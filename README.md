# Student Management System

A complete web application for managing student details, categories, and achievements.

## Tech Stack
- **Backend:** Python 3, Django
- **Database:** MySQL
- **Frontend:** HTML5, CSS3, Bootstrap 5

## Setup Instructions

### 1. Database Configuration
Ensure MySQL is installed and running. Login to your MySQL server and create the database:
```sql
CREATE DATABASE student_management_db;
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

### 5. Run the Server
```bash
python manage.py runserver
```

### 6. Access the Application
- **Dashboard:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## Configuration

All credentials are read from environment variables (via `python-dotenv`), never hardcoded. Copy `.env.example` to `.env` and fill in your own values:
```bash
cp .env.example .env
```
- `DB_*` — your local MySQL connection details.
- `DJANGO_SECRET_KEY` — optional; if unset, a random key is generated each time the app starts (fine for local dev, but sessions won't survive a restart).
- `ADMIN_*` — used only by `reset_admin.py` (see below); required to run that script.

`.env` is gitignored and should never be committed.

## Resetting the admin user

`reset_admin.py` creates/resets a superuser using `ADMIN_USERNAME`, `ADMIN_EMAIL`, and `ADMIN_RESET_PASSWORD` from your `.env` file:
```bash
python reset_admin.py
```
