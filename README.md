# 🏥 Advanced Hospital Management System

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Open Issues](https://img.shields.io/github/issues/Maaz-Saeed/hospital-management-system)](https://github.com/Maaz-Saeed/hospital-management-system/issues)
[![Last Commit](https://img.shields.io/github/last-commit/Maaz-Saeed/hospital-management-system)](https://github.com/Maaz-Saeed/hospital-management-system/commits/main)

A production-ready web application built with **Python Flask** and **SQLite** for managing a hospital's digital presence, patient communications, and internal operations.

---

## 📋 Project Overview

| Field | Details |
|-------|---------|
| Developer | Maooz Khan |
| Registration No. | SU-23-01-002-033 |
| Semester | 5th |
| Department | Computer Science |
| Tech Stack | Python Flask, SQLite, HTML5, CSS3, JavaScript |

---

## ✨ Features

- **Hospital Website** – Professional multi-page website (Home, About, Services, Contact)
- **Authentication System** – Secure register/login with hashed passwords & session management
- **Role-Based Access** – Admin and User roles with protected routes
- **AI Chatbot** – Rule-based FAQ chatbot with AJAX-powered chat UI
- **Admin Dashboard** – View contact messages, chatbot logs, and registered users
- **Student Portfolio** – Developer portfolio page
- **Responsive Design** – Mobile-friendly modern UI

---

## 📁 Project Structure

```
hospital_system/
├── app.py                  # Application factory
├── config.py               # Configuration settings
├── models.py               # SQLAlchemy database models
├── routes/
│   ├── __init__.py
│   ├── main_routes.py      # Public website routes
│   ├── auth_routes.py      # Authentication routes
│   ├── admin_routes.py     # Admin-only routes
│   └── chatbot_routes.py   # Chatbot API & page
├── static/
│   ├── css/style.css       # Main stylesheet
│   └── js/script.js        # Frontend JavaScript
├── templates/
│   ├── base.html           # Layout template
│   ├── index.html          # Home page
│   ├── about.html          # About page
│   ├── services.html       # Services/Departments
│   ├── contact.html        # Contact form
│   ├── chatbot.html        # Chatbot interface
│   ├── portfolio.html      # Developer portfolio
│   ├── login.html          # Login form
│   ├── register.html       # Registration form
│   ├── dashboard.html      # User dashboard
│   ├── admin_dashboard.html # Admin panel
│   ├── 404.html            # Not found page
│   └── 500.html            # Server error page
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone / Download the Project

```bash
cd hospital_system
```

### 2. Create & Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask flask-sqlalchemy werkzeug
```

Or using a requirements file:
```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Visit: **http://localhost:5000**

---

## 📦 Requirements

```
flask>=2.3.0
flask-sqlalchemy>=3.0.0
werkzeug>=2.3.0
```

Generate with:
```bash
pip freeze > requirements.txt
```

---

## 🗄️ Database

- SQLite database (`hospital.db`) is **auto-created** on first run
- Tables created automatically via SQLAlchemy's `db.create_all()`
- Default admin account is seeded automatically

### Tables

| Table | Description |
|-------|-------------|
| `users` | Registered users with hashed passwords |
| `contact_messages` | Messages submitted via contact form |
| `chatbot_logs` | Chatbot query/response history |

---

## 🔐 Default Admin Account

```
Email:    admin@hospital.com
Password: admin123
```

> ⚠️ **Change this password in production!**

---

## 🤖 Chatbot Topics

The chatbot handles the following queries:
- Departments / specialties
- Hospital timings
- Emergency contact
- Doctor availability
- Location & directions
- Fees & charges
- Insurance information
- General greetings

---

## 🛡️ Security Features

- Passwords hashed using Werkzeug's `generate_password_hash`
- SQL injection prevention via SQLAlchemy ORM
- Session-based authentication
- Role-based access control with decorators
- Form validation (client + server-side)
- Custom 404/500 error pages

---

## 🔮 Future Improvements

- [ ] Appointment booking system with calendar
- [ ] Patient records management
- [ ] Doctor profiles and scheduling
- [ ] Email notifications (Flask-Mail)
- [ ] JWT-based API for mobile apps
- [ ] Medical reports upload/download
- [ ] Payment gateway integration
- [ ] SMS notifications via Twilio

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

*Built with ❤️ by Maooz Khan | SU-23-01-002-033*
