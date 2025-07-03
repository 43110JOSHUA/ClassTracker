import sqlite3

connection = sqlite3.connect('class2023.db')
cursor = connection.cursor()

# Create database
create_command = """CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    out_of_state INTEGER NOT NULL,
    went_to_university INTEGER NOT NULL,
    university_name TEXT,
    occupation TEXT NOT NULL 
    )"""

cursor.execute(create_command)