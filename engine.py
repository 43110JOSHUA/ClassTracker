# This module handles interactions with the database and interface, and runs the main program

import sqlite3
import interface

db_name = 'yourClassData.db' # Edit this if you want a different file name

def main():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # STEP 1: Create Database
    create_command = """CREATE TABLE IF NOT EXISTS classmates(
        classmate_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        user_in = input("\nCommand: ")
        if user_in == '1':
            add_row(cursor, connection)

        elif user_in == '2':
            remove_row(cursor, connection)

        elif user_in == '3':
            pass

        elif user_in == '4':
            pass

        elif user_in == '5':
            pass

        elif user_in == '6':
            pass

        elif user_in == '7':
            interface.quit()
            break

        else:
            interface.invalid_command()
            interface.help()

    # STEP 3: Close Connection
    connection.close()


def add_row(cursor, connection):
    """This function adds a row to a database"""
    new_classmate = interface.new_data()
    cursor.execute("""
        INSERT INTO classmates (name, out_of_state, occupation, went_to_university, university_name)
        VALUES (?, ?, ?, ?, ?)""",
        (new_classmate.name, int(new_classmate.out_of_state), new_classmate.occupation, int(new_classmate.went_to_university),
        new_classmate.university_name))
    connection.commit()
    interface.successfully_added(new_classmate)


def remove_row(cursor, connection):
    """This function removes a specified row from a database"""
    id_to_remove = interface.remove_data()
    cursor.execute(f"SELECT name FROM classmates WHERE classmate_id = {id_to_remove}")
    classmate_to_remove = cursor.fetchone()

    if (classmate_to_remove):
        cursor.execute(f"DELETE FROM classmates WHERE classmate_id = {id_to_remove}")
        connection.commit()
        interface.successfully_removed(classmate_to_remove[0])
    else: # id doesn't exist
        interface.failure_remove(id_to_remove)


def search_row():
    pass


def calc_stats():
    pass


if __name__ == "__main__":
    main()