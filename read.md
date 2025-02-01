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

![Upload CSV](sandbox:/mnt/data/Screenshot%202025-02-02%20025438.png)

### **2. Retrieving Movies**

![Get Movies](sandbox:/mnt/data/Screenshot%202025-02-02%20025445.png)

### **3. Filtering and Sorting Movies**

![Filtered Movies](sandbox:/mnt/data/Screenshot%202025-02-02%20025454.png)

## Submission Guidelines

- Ensure that the repository contains the following:
  - **Flask API Code** for handling CSV upload and data retrieval.
  - **README** with comprehensive setup and API usage documentation.
  - **Postman Collection** for API testing.
- Follow best practices in coding, API design, and documentation.

---

**Author:** Your Name

**Author:** Rishika Carpenter
