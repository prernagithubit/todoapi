# 📝 Todo API

A fast, lightweight REST API built with **FastAPI** and **SQLAlchemy**.

---

## 🚀 Tech Stack

- **FastAPI** — Modern Python web framework
- **SQLAlchemy** — Database ORM
- **SQLite** — Lightweight database
- **Pydantic** — Data validation
- **Uvicorn** — ASGI server

---

## ✨ Features

- ✅ Create a todo
- ✅ Get all todos
- ✅ Mark todo as complete
- ✅ Delete a todo
- ✅ Auto-generated Swagger docs

---
## 📁 Project Structure

```
todoapi/
├── main.py              # App entry point & route registration
├── database.py          # Database connection & session
├── models.py            # Database table definitions
├── schemas.py           # Pydantic request/response schemas
├── auth.py              # JWT token creation & verification
├── hashing.py           # Password hashing & verification
├── requirements.txt     # Project dependencies
├── .gitignore           # Files to ignore in git
└── routers/
    ├── __init__.py      # Makes routers a Python package
    ├── todos.py         # Todo CRUD routes
    └── users.py         # User signup & login routes
```
---

## ⚙️ How to Run

# Clone the repo
git clone https://github.com/prernagithubit/todoapi.git
cd todoapi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic

# Run the server
uvicorn main:app --reload



## 📖 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos` | Get all todos |
| POST | `/todos` | Create a todo |
| PUT | `/todos/{id}` | Mark as complete |
| DELETE | `/todos/{id}` | Delete a todo |

---

## 📄 API Docs

Once the server is running, open:
- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

---
## 🌍 Live API
- Live URL → https://todoapi-1-bbkz.onrender.com
- Live Docs → https://todoapi-1-bbkz.onrender.com/docs