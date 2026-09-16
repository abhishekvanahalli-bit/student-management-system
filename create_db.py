import os

import MySQLdb
from dotenv import load_dotenv

load_dotenv()

# Database configuration from your request
db_config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'passwd': os.environ['DB_PASSWORD'],
    'port': int(os.environ.get('DB_PORT', 3306)),
}

try:
    # Connect to MySQL without specifying a database
    db = MySQLdb.connect(**db_config)
    cursor = db.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS student_management_db")
    print("Database 'student_management_db' created successfully!")

    db.close()
except Exception as e:
    print(f"Error creating database: {e}")
