import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT,
    year INTEGER,
    email TEXT UNIQUE,
    phone TEXT
)
""")

conn.commit()

def add_student():
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    year = input("Enter Year: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    cursor.execute("INSERT INTO students (name, department, year, email, phone) VALUES (?, ?, ?, ?, ?)",
                   (name, dept, year, email, phone))
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_student():
    sid = input("Enter Student ID to update: ")
    new_year = input("Enter new Year: ")

    cursor.execute("UPDATE students SET year=? WHERE student_id=?", (new_year, sid))
    conn.commit()
    print("Student updated!")

def delete_student():
    sid = input("Enter Student ID to delete: ")

    cursor.execute("DELETE FROM students WHERE student_id=?", (sid,))
    conn.commit()
    print("Student deleted!")

while True:
    print("\n--- Student Manager ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")

conn.close()

