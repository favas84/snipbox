# SnipBox - A Simple Snippet Saving App

SnipBox is a Django-based API that allows users to save and manage short text snippets with tags. It supports **JWT authentication**, **PostgreSQL database**, and is containerized using **Docker**.

---

## Features
- Save text snippets with **title, note, and tags**.
- **JWT authentication** for user management.
- Uses **Django REST Framework (DRF)**.
- **PostgreSQL** as the database.
- **Dockerized setup** for easy deployment.

---

## Requirements
Before installing, ensure you have the following installed:

Requirement 
| Python          | 3.9+    |
| Docker          | Latest  |
| Docker Compose  | Latest  |

---

## Clone the Repository

git clone https://github.com/yourusername/snipbox.git
cd snipbox

## Set Up the Environment Variables

DB_HOST=db
DB_NAME=snippetdb
DB_USER=snippetuser
DB_PASS=changeme
SECRET_KEY=your_django_secret_key_here
DEBUG=True

## Run the Application with Docker

docker-compose up --build

## Running Database Migrations

docker-compose exec app python manage.py migrate

## Create a Superuser (Admin)

docker-compose exec app python manage.py createsuperuser