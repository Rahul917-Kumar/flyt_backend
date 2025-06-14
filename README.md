# 🛠️ Drone Mission Backend

This is the backend API for the Drone Mission Management System. It enables organizations to plan, manage, and monitor drone missions using a RESTful API and automated simulation via cron jobs.

## 🚀 Features

- Drone and Mission CRUD APIs
- Real-time mission progress simulation
- Mission lifecycle control: pause, resume, abort
- Scheduled cron jobs using `django-crontab`

---

## 🔧 Tech Stack

- Django + Django REST Framework
- PostgreSQL / SQLite
- Django Crontab

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <folder_name>/

2.
  ```bash
  python3 -m venv venv
  source venv/bin/activate

  pip install -r requirements.txt

  python manage.py migrate
  
  python manage.py runserver
  
  python manage.py crontab add

