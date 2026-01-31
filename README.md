Todo Web App

A simple web application for managing personal to-do lists.
Each user has their own tasks and cannot see others' todos.

Built with Django + DRF for backend and React for frontend.
JWT is used for authentication, Swagger for API docs.

Features:
- User registration & authentication
- CRUD operations for todos
- JWT authentication
- Swagger UI for API testing

Tech Stack:
- Python 3.13
- Django 6.0
- Django REST Framework
- drf-yasg (Swagger)
- djangorestframework-simplejwt (JWT)

Setup:

1. Clone repo and navigate to backend:
   git clone https://github.com/<your-username>/todo-web-drf-react.git
   cd back

2. Create virtual environment and install dependencies:
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   pip install -r requirements.txt

3. Run migrations:
   python manage.py migrate

4. Create superuser:
   python manage.py createsuperuser

5. Run server:
   python manage.py runserver

API Endpoints:
- Swagger UI: http://127.0.0.1:8000/swagger/
- /api/todos/          - list & create todos
- /api/todos/<id>/     - retrieve, update, delete todos
- /api/token/          - get JWT token
- /api/token/refresh/  - refresh JWT token
