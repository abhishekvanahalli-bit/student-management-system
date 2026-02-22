import MySQLdb

# Database configuration from your request
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '***REMOVED***',
    'port': 3306
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
