# This module runs the main program

import sqlite3
import interface

db_name = 'yourClassData.db' # Edit this if you want a different file name

def add_row():
    pass


def remove_row():
    pass


def calc_stats():
    pass


if __name__ == "__main__":
    connection = sqlite3.connect(db_name)
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
    interface.help()
    while True:
        user_in = input()
        if user_in == '1':
            interface.new_data()

        elif user_in == '2':
            pass

        elif user_in == '3':
            pass

        elif user_in == '4':
            interface.quit()
            break

        else: # invalid input
            interface.help()

    # STEP 3: Close Connection
    connection.close()

