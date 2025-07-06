# This module handles interactions with the database and interface, and runs the main program

import sqlite3
import interface
from classmate import Classmate

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
        user_in = interface.command_input()
        if user_in == '1':
            add_row(cursor, connection)

        elif user_in == '2':
            remove_row(cursor, connection)

        elif user_in == '3':
            edit_row(cursor, connection)

        elif user_in == '4':
            search_row(cursor)

        elif user_in == '5':
            view_all(cursor)

        elif user_in == '6':
            calc_stats(cursor)

        elif user_in == '7':
            interface.quit()
            break

        else:
            interface.invalid_command()
            interface.help()

    # STEP 3: Close Connection
    connection.close()


def add_row(cursor, connection):
    """This function adds a row to a database."""
    new_classmate = interface.new_data()

    cursor.execute("""
        INSERT INTO classmates (name, out_of_state, occupation, went_to_university, university_name)
        VALUES (?, ?, ?, ?, ?)""",
        (new_classmate.name, int(new_classmate.out_of_state), new_classmate.occupation, int(new_classmate.went_to_university),
        new_classmate.university_name))
    connection.commit()

    interface.successfully_action(new_classmate, "added")


def remove_row(cursor, connection):
    """This function removes a specified row from a database."""
    id_to_remove = interface.request_id("remove")
    classmate_to_remove = _retrieve_row(cursor, id_to_remove)

    if (classmate_to_remove):
        cursor.execute("DELETE FROM classmates WHERE classmate_id = ?", (id_to_remove,))
        connection.commit()
        interface.successfully_action(classmate_to_remove, "removed")

    else: # id doesn't exist
        interface.failure_id(id_to_remove)


def edit_row(cursor, connection):
    """This function edits an existing row in the database."""
    id_to_edit = interface.request_id("edit")
    classmate_to_edit = _retrieve_row(cursor, id_to_edit)

    if (classmate_to_edit):
        editted_classmate = interface.new_data()
        cursor.execute("UPDATE classmates SET name = ?, out_of_state = ?, occupation = ?, went_to_university = ?," \
        "university_name = ? WHERE classmate_id = ?", (editted_classmate.name, int(editted_classmate.out_of_state),
                                                       editted_classmate.occupation, int(editted_classmate.went_to_university),
                                                       editted_classmate.university_name, id_to_edit))
        connection.commit()

    else:
        interface.failure_id(id_to_edit)


def search_row(cursor):
    """Searches and displays all classmates based on provided name."""
    name = interface.request_name()
    cursor.execute("SELECT * FROM classmates WHERE name LIKE ?", (f"%{name}%",))
    db_data = cursor.fetchall()
    
    interface.print_table(db_data)


def view_all(cursor):
    """Displays all classmates in the database in a table format."""
    cursor.execute("SELECT * FROM classmates")
    db_data = cursor.fetchall()
    
    interface.print_table(db_data)


def calc_stats():
    """Calculates and displays statistics."""
    pass


# HELPERS
def _retrieve_row(cursor, id_num: int) -> Classmate:
    """This helper function retrieves a row given an ID number and returns entry as a Classmate object."""
    cursor.execute("SELECT * FROM classmates WHERE classmate_id = ?", (id_num,))
    classmate_found = cursor.fetchone()

    if classmate_found:
        return Classmate(classmate_found[0], classmate_found[1], classmate_found[2], classmate_found[3],
                         classmate_found[4], classmate_found[5])
    else: 
        return None


if __name__ == "__main__":
    main()