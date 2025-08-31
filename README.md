# Task Management API

This is a simple Task Management API built with Django and Django REST Framework.

## Features
- User authentication
- CRUD operations for tasks
- CRUD operations for categories (optional stretch goal)
- Mark tasks as complete or incomplete
- Filter tasks by status, priority, and due date

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Start server: `python manage.py runserver`

## API Endpoints
- `/api/tasks/`
- `/api/categories/`

