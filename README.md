# ✅ Todo Manager API

A simple RESTful API built with Django and Django REST Framework that allows authenticated users to manage their personal to-do tasks.

---

## 🚀 Features

- User Registration and Login (Token-based Authentication)
- CRUD operations for Todo Tasks
- Tasks have status, due date, and optional completion tracking
- API protected via authentication
- Frontend page to interact with tasks
- Postman-friendly endpoints

---

## 🏗️ Project Structure

todoapi/
├── todo/ # Main app with models, serializers, views
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── route.py
│ └── templates/todo/todo_frontend.html
├── todoapi/ # Project settings
│ ├── settings.py
│ ├── urls.py
├── db.sqlite3 # Default database
├── manage.py
└── README.md
