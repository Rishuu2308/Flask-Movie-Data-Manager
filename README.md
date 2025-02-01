# IMDb Content Upload and Review System

## Overview

This project implements a **Flask-based API** designed for managing movie data. The system allows users to upload CSV files containing movie details and retrieve the stored data with advanced filtering, sorting, and pagination options.

## Features

- **CSV Upload API** to store movie-related data in MongoDB.
- **Movie Retrieval API** with:
  - **Pagination** to handle large datasets efficiently.
  - **Filtering** by `year_of_release` and `language`.
  - **Sorting** by `release_date` and `ratings` in ascending or descending order.

## Technology Stack

- **Programming Language:** Python
- **Framework:** Flask
- **Database:** MongoDB
- **Libraries:** Pandas, Flask-PyMongo, Werkzeug

## Setup Instructions

### 1. Install Dependencies

Ensure Python is installed, then execute:

```bash
pip install flask pymongo pandas werkzeug
```

### 2. Configure and Start MongoDB

Ensure MongoDB is installed and running:

```bash
mongod --dbpath /path/to/db
```

### 3. Run the Flask Application

```bash
python app.py
```

The API will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Upload CSV File

**Endpoint:**

```http
POST /upload
```

**Request:**

- Form-data: `file` (CSV file containing movie details)

**Response:**

```json
{
  "message": "File uploaded and data stored successfully"
}
```

### 2. Retrieve Movies

**Endpoint:**

```http
GET /movies?page=1&per_page=10&year=1995&language=English&sort_by=release_date&order=asc
```

**Query Parameters:**

- `page`: (Optional) Page number for pagination.
- `per_page`: (Optional) Number of results per page.
- `year`: (Optional) Filter by release year.
- `language`: (Optional) Filter by language.
- `sort_by`: (Optional) Sorting field (`release_date` or `ratings`).
- `order`: (Optional) Sorting order (`asc` or `desc`).

**Response:**

```json
[
  {
    "_id": "123456",
    "title": "Toy Story",
    "release_date": "1995-10-30",
    "year_of_release": 1995,
    "language": "English",
    "ratings": 7.7
  }
]
```

## Testing with Postman

1. Import the provided **Postman collection**.
2. Use the `/upload` endpoint to upload a CSV file.
3. Query movies using `/movies` with various filters and sorting options.

## Proof of Implementation

Below are screenshots demonstrating the successful implementation of the system:

### **1. Uploading CSV File**

![Image](https://github.com/user-attachments/assets/836f4d7d-fd46-425f-89e0-a223324e2c2b)
### **2. Retrieving Movies**
![Image](https://github.com/user-attachments/assets/7d8b52f8-5356-4651-833f-0ff42f71ebdd)


### **3. Filtering and Sorting Movies**
![Image](https://github.com/user-attachments/assets/80bfc9d2-6ef5-4939-92ac-e567204827dd)



**Author:** Rishika Carpenter
