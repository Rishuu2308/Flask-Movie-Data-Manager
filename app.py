from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
import pandas as pd
import os
from bson.json_util import dumps
from pymongo import ASCENDING, DESCENDING


# Initialize Flask app
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/imdb_db"
mongo = PyMongo(app)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'

@app.route("/upload", methods=["POST"])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Read CSV and insert into MongoDB
        df = pd.read_csv(filepath)
        df['year_of_release'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
        movies = df.to_dict(orient='records')
        mongo.db.movies.insert_many(movies)
        
        return jsonify({"message": "File uploaded and data stored successfully"})
    
    return jsonify({"error": "Invalid file format. Only CSV allowed"}), 400

@app.route("/movies", methods=["GET"])
def get_movies():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    year = request.args.get("year")
    language = request.args.get("language")
    sort_by = request.args.get("sort_by", "release_date")
    order = request.args.get("order", "asc")

    query = {}
    if year:
        query["year_of_release"] = int(year)
    if language:
        query["languages"] = {"$regex": language, "$options": "i"}

    sort_fields = {"release_date": "release_date", "ratings": "vote_average"}
    sort_order = ASCENDING if order == "asc" else DESCENDING

    if sort_by in sort_fields:
        sort_field = sort_fields[sort_by]
    else:
        sort_field = "release_date"

    movies = list(mongo.db.movies.find(query).sort(sort_field, sort_order)
                                     .skip((page - 1) * per_page)
                                     .limit(per_page))
    
    for movie in movies:
        movie["_id"] = str(movie["_id"])
    
    return jsonify(movies)

if __name__ == "__main__":
    app.run(debug=True)
