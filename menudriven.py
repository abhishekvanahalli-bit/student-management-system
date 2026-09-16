import os
from datetime import datetime
import mysql.connector
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# ==================================================
# MYSQL CONNECTION
# ==================================================
# Set DB_PASSWORD (and optionally DB_HOST/DB_USER) in your local .env file

mysql_db = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", "")
)

mysql_cursor = mysql_db.cursor()

# Database
mysql_cursor.execute("CREATE DATABASE IF NOT EXISTS student_management_db")
mysql_cursor.execute("USE student_management_db")

# Table
mysql_cursor.execute("""
CREATE TABLE IF NOT EXISTS student_achievements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    reg_no VARCHAR(50) UNIQUE,
    course VARCHAR(100),
    batch VARCHAR(20),
    department VARCHAR(100),
    status VARCHAR(20),
    created_at DATETIME
)
""")
mysql_db.commit()

print("MySQL Database & Table Ready")

# ==================================================
# MONGODB CONNECTION
# ==================================================

mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["student_management_db"]
mongo_col = mongo_db["student_achievements"]

# ==================================================
# MYSQL FUNCTIONS
# ==================================================

def mysql_insert():
    sql = """
    INSERT INTO student_achievements
    (name,email,reg_no,course,batch,department,status,created_at)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    data = (
        input("Name: "),
        input("Email: "),
        input("Register No: "),
        input("Course: "),
        input("Batch: "),
        input("Department: "),
        input("Status: "),
        datetime.now()
    )
    try:
        mysql_cursor.execute(sql, data)
        mysql_db.commit()
        print("MySQL Record Inserted")
    except mysql.connector.Error as e:
        print("Error:", e)

def mysql_view():
    mysql_cursor.execute("SELECT * FROM student_achievements")
    rows = mysql_cursor.fetchall()
    if not rows:
        print("⚠️ No records found")
    for r in rows:
        print(r)

def mysql_update():
    reg = input("Enter Register No to Update: ")
    new_status = input("Enter New Status: ")

    mysql_cursor.execute(
        "UPDATE student_achievements SET status=%s WHERE reg_no=%s",
        (new_status, reg)
    )
    mysql_db.commit()

    if mysql_cursor.rowcount > 0:
        print("MySQL Record Updated")
    else:
        print("No record found with this Register No")

def mysql_delete():
    reg = input("Enter Register No to Delete: ")

    mysql_cursor.execute(
        "DELETE FROM student_achievements WHERE reg_no=%s",
        (reg,)
    )
    mysql_db.commit()

    if mysql_cursor.rowcount > 0:
        print("MySQL Record Deleted")
    else:
        print("No record found with this Register No")

def mysql_filter():
    dept = input("Enter Department: ")
    mysql_cursor.execute(
        "SELECT * FROM student_achievements WHERE department=%s",
        (dept,)
    )
    rows = mysql_cursor.fetchall()
    if not rows:
        print("⚠️ No records found")
    for r in rows:
        print(r)

def mysql_aggregate():
    mysql_cursor.execute(
        "SELECT department, COUNT(*) FROM student_achievements GROUP BY department"
    )
    for r in mysql_cursor.fetchall():
        print("Department:", r[0], "| Total:", r[1])

# ==================================================
# MONGODB FUNCTIONS
# ==================================================

def mongo_insert():
    reg = input("Register No: ")
    if mongo_col.find_one({"reg_no": reg}):
        print("Register No already exists")
        return

    doc = {
        "name": input("Name: "),
        "email": input("Email: "),
        "reg_no": reg,
        "course": input("Course: "),
        "batch": input("Batch: "),
        "department": input("Department: "),
        "status": input("Status: "),
        "created_at": datetime.now()
    }
    mongo_col.insert_one(doc)
    print("MongoDB Record Inserted")

def mongo_view():
    data = list(mongo_col.find())
    if not data:
        print("⚠️ No records found")
    for d in data:
        print(d)

def mongo_update():
    reg = input("Enter Register No to Update: ")
    new_status = input("Enter New Status: ")

    result = mongo_col.update_one(
        {"reg_no": reg},
        {"$set": {"status": new_status}}
    )

    if result.matched_count > 0:
        print("MongoDB Record Updated")
    else:
        print("No record found with this Register No")

def mongo_delete():
    reg = input("Enter Register No to Delete: ")

    result = mongo_col.delete_one({"reg_no": reg})

    if result.deleted_count > 0:
        print("MongoDB Record Deleted")
    else:
        print("No record found with this Register No")

def mongo_filter():
    dept = input("Enter Department: ")
    data = list(mongo_col.find({"department": dept}))
    if not data:
        print("⚠️ No records found")
    for d in data:
        print(d)

def mongo_aggregate():
    pipeline = [
        {"$group": {"_id": "$department", "total": {"$sum": 1}}}
    ]
    for r in mongo_col.aggregate(pipeline):
        print("Department:", r["_id"], "| Total:", r["total"])

# ==================================================
# MAIN MENU
# ==================================================

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. MySQL Insert")
    print("2. MySQL View")
    print("3. MySQL Update")
    print("4. MySQL Delete")
    print("5. MySQL Filter")
    print("6. MySQL Aggregate")
    print("7. MongoDB Insert")
    print("8. MongoDB View")
    print("9. MongoDB Update")
    print("10. MongoDB Delete")
    print("11. MongoDB Filter")
    print("12. MongoDB Aggregate")
    print("13. Exit")

    choice = input("Enter your choice: ")

    if choice == "1": mysql_insert()
    elif choice == "2": mysql_view()
    elif choice == "3": mysql_update()
    elif choice == "4": mysql_delete()
    elif choice == "5": mysql_filter()
    elif choice == "6": mysql_aggregate()
    elif choice == "7": mongo_insert()
    elif choice == "8": mongo_view()
    elif choice == "9": mongo_update()
    elif choice == "10": mongo_delete()
    elif choice == "11": mongo_filter()
    elif choice == "12": mongo_aggregate()
    elif choice == "13":
        print("Program Closed Successfully")
        break
    else:
        print("Invalid Choice")