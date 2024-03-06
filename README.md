
## Django CRUD Operations

This is a simple Django project demonstrating CRUD (Create, Read, Update, Delete) operations using Django.

## Installation

1. Clone the repository:

   git clone https://github.com/your_username/django-crud.git
## Navigate into the project directory:

cd django-crud
## Create a virtual environment:

python -m venv env
## Activate the virtual environment:
## On Windows:

.\env\Scripts\activate
## On macOS and Linux:

source env/bin/activate
## Install the required dependencies:

pip install -r requirements.txt
Run migrations:

python manage.py migrate
## Start the development server:

python manage.py runserver
Open your web browser and go to http://localhost:8000/ to view the application.

## Usage
The application provides endpoints for CRUD operations on a sample model. You can perform the following actions:
Create: Add new records to the database.
Read: View existing records.
Update: Modify existing records.
Delete: Remove records from the database.

## Technologies Used
Python
Django
SQLite (default database)

## Project Structure
crud_app/: Django application directory.
crud_project/: Django project directory.
templates/: HTML templates for rendering pages.
static/: Static files like CSS, JavaScript, etc.
