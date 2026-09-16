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

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and fill in your own values (`.env` is gitignored and must never be committed):
```bash
cp .env.example .env
```
Generate a fresh `DJANGO_SECRET_KEY` (do not reuse the example placeholder), and set `DB_PASSWORD` to your local MySQL password.

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

### 7. Run the Server
```bash
python manage.py runserver
```

### 8. Access the Application
- **Dashboard:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## Configuration

Database and secret-key values are read from environment variables (see `.env.example`) — nothing sensitive is hardcoded in `settings.py`.
