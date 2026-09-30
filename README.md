# Recipe API

A RESTful Recipe API built with **Django** and **Django REST Framework (DRF)**.

This project was built as backend practice to develop practical experience with REST APIs, serializers, authentication, query parameters, filtering, searching, ordering, pagination, and API testing.

## Features

* Create recipes through the API
* Retrieve recipes
* Update and delete recipes
* JWT authentication
* Protected API endpoints
* Recipe serialization and validation
* Filter recipes by:

  * Name
  * Price
* Search recipes by:

  * Name
  * Description
* Order recipes by:

  * Name
  * Price
* Ascending and descending ordering
* Page-number pagination
* API testing with Postman

## Tech Stack

* **Python**
* **Django**
* **Django REST Framework**
* **Django ORM**
* **JWT Authentication**
* **PostgreSQL / SQLite**
* **Postman**
* **Git & GitHub**

## Example API Requests

### Get all recipes

```http
GET /api/
```

### Filter by name

```http
GET /api/?name=Pizza
```

### Filter by price

```http
GET /api/?price=10
```

### Search recipes

Searches both the recipe name and description.

```http
GET /api/?search=cheese
```

### Order by price

Ascending:

```http
GET /api/?ordering=price
```

Descending:

```http
GET /api/?ordering=-price
```

### Pagination

```http
GET /api/?page=2
```

### Combine query parameters

The API allows filtering, searching, ordering and pagination to be combined.

```http
GET /api/?name=Pizza&search=cheese&ordering=-price&page=2
```

## Example Response

```json
{
    "count": 3,
    "next": "http://127.0.0.1:8000/api/?page=2",
    "previous": null,
    "results": [
        {
            "name": "Fish and Chips",
            "description": "Boil fish and chips",
            "price": "9.23"
        }
    ]
}
```

## Project Structure

```text
recipe-api/
│
├── manage.py
│
├── recipe/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

> The exact structure may vary depending on the current project configuration.

## Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd recipe-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will then be available at:

```text
http://127.0.0.1:8000/
```

## Authentication

The API uses JWT authentication for protected endpoints.

Clients can obtain an access token and refresh token through the authentication endpoints.

The access token is then included in requests using:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## What I Practiced

This project helped me practise several backend concepts:

* Designing REST API endpoints
* Django models
* Django REST Framework serializers
* Serializer validation
* HTTP methods and status codes
* Query parameters
* Django QuerySets
* `Q` objects
* Case-insensitive searching with `icontains`
* Filtering
* Ordering
* Pagination
* JWT authentication
* API permissions
* Testing APIs with Postman
* Git version control

## Future Improvements

Possible future improvements include:

* Convert the current function-based views to class-based DRF views
* Add more advanced filtering
* Add categories for recipes
* Add recipe ownership so users can manage their own recipes
* Add automated tests
* Add API documentation with Swagger/OpenAPI
* Deploy the API
* Add filtering by multiple fields
* Improve error handling and validation

## Status

**Completed as a Django REST Framework learning project.**

The project will continue to be improved as I learn more about Django REST Framework and backend development.
