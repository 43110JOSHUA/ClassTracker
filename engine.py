# This module runs the main program
import sqlite3
from interface import *

connection = sqlite3.connect('yourClassData.db')
cursor = connection.cursor()

# STEP 1: Create Database
create_command = """CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    out_of_state INTEGER NOT NULL,
    occupation TEXT NOT NULL ,
    went_to_university INTEGER NOT NULL,
    university_name TEXT
    )"""
cursor.execute(create_command)
connection.commit()

# STEP 2: Main Loop
help()
while True:
    break


# STEP 3: Close Connection
connection.close()

