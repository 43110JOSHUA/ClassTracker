# This module handles interactions with the database and interface, and runs the main program

import sqlite3
import interface
import stats
from classmate import Classmate

# --- Configuration ---
db_name = 'yourClassData.db'  # Edit this if you want a different file name
create_command = """CREATE TABLE IF NOT EXISTS classmates(
        classmate_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        out_of_state INTEGER NOT NULL,
        occupation TEXT,
        went_to_university INTEGER NOT NULL,
        university_name TEXT
        )"""

# --- Helper Functions ---
def _retrieve_row(cursor, id_num: int) -> Classmate:
    """Retrieve a row given an ID and return it as a Classmate object."""
    cursor.execute("SELECT * FROM classmates WHERE classmate_id = ?", (id_num,))
    classmate_found = cursor.fetchone()

    if classmate_found:
        return Classmate(classmate_found[0], classmate_found[1], classmate_found[2], classmate_found[3],
                         classmate_found[4], classmate_found[5])
    else:
        return None

def _convert_to_classmate(data: list[list]) -> list[Classmate]:
    """Convert a list of raw tuples (from the database) into a list of Classmate objects."""
    return [Classmate(*row) for row in data]

# --- Core Functions ---
def add_row(cursor, connection):
    """Prompt the user for new classmate data and insert it into the database.
    Commits the change after successful insertion."""
    new_classmate = interface.new_data()

    cursor.execute("""
        INSERT INTO classmates (name, out_of_state, occupation, went_to_university, university_name)
        VALUES (?, ?, ?, ?, ?)""",
        (new_classmate.name, new_classmate.out_of_state, new_classmate.occupation, new_classmate.went_to_university,
         new_classmate.university_name))
    connection.commit()

    interface.successfully_action(new_classmate, "added")

def remove_row(cursor, connection):
    """Prompt the user for an ID and remove the corresponding classmate entry from the database.
    Displays success or failure message based on ID existence."""
    id_to_remove = interface.request_id("remove")
    classmate_to_remove = _retrieve_row(cursor, id_to_remove)

    if classmate_to_remove:
        cursor.execute("DELETE FROM classmates WHERE classmate_id = ?", (id_to_remove,))
        connection.commit()
        interface.successfully_action(classmate_to_remove, "removed")
    else:
        interface.failure_id(id_to_remove)

def edit_row(cursor, connection):
    """Prompt the user for an ID and update the corresponding classmate entry in the database.
    Replaces the existing entry with new user-provided values."""
    id_to_edit = interface.request_id("edit")
    classmate_to_edit = _retrieve_row(cursor, id_to_edit)

    if classmate_to_edit:
        editted_classmate = interface.new_data()
        cursor.execute("""
            UPDATE classmates 
            SET name = ?, out_of_state = ?, occupation = ?, went_to_university = ?, university_name = ?
            WHERE classmate_id = ?
        """, (editted_classmate.name, editted_classmate.out_of_state,
              editted_classmate.occupation, editted_classmate.went_to_university,
              editted_classmate.university_name, id_to_edit))
        connection.commit()
        interface.successfully_action(classmate_to_edit, "editted")
    else:
        interface.failure_id(id_to_edit)

def search_row(cursor):
    """Prompt the user for a name (or partial name), search for matching entries in the database,
    and display results in a formatted table."""
    name = interface.request_name()
    cursor.execute("SELECT * FROM classmates WHERE name LIKE ?", (f"%{name}%",))
    db_data = cursor.fetchall()
    classmate_data = _convert_to_classmate(db_data)

    interface.print_table(classmate_data)

def view_all(cursor):
    """Retrieve and display all classmate entries from the database in a formatted table."""
    cursor.execute("SELECT * FROM classmates")
    db_data = cursor.fetchall()
    classmate_data = _convert_to_classmate(db_data)

    interface.print_table(classmate_data)

def calc_stats(cursor):
    """Retrieve all classmate entries from the database, compute statistics,
    and display the results using the interface module."""
    cursor.execute("SELECT * FROM classmates")
    db_data = cursor.fetchall()
    classmate_data = _convert_to_classmate(db_data)

    compiled_stats = stats.compute_stats(classmate_data)
    interface.print_stats(compiled_stats)

# --- Main Program ---
def main():
    """Run the main loop of the program. Connects to the database, creates the table if it doesn't exist, 
    and handles user input until the program is exited."""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # STEP 1: Create Database
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

if __name__ == "__main__":
    main()