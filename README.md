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

## Week 4 Progress

This week, I focused on improving the Task Management API by implementing serializers with nested relationships and running automated tests.

### Highlights
- Implemented `TaskSerializer` with support for `User` and `Category` relationships.
- Wrote and executed 5 API tests (`create`, `list`, `retrieve`, `update`, `delete`).
- 3 out of 5 tests passed successfully.
- Identified issues with `create` and `update` endpoints (returning 400 Bad Request).
- Pushed code updates to GitHub for version tracking.

### Challenges
- Difficulty balancing nested serializer outputs with writable fields for foreign keys.
- Debugging validation errors that prevented some tests from passing.

### Next Steps
- Debug failing tests by printing error responses.
- Improve serializer design for both reading and writing.
- Deploy the project and record a demo video.

