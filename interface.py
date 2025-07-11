# This module contains user interface functions handling I/O

from classmate import Classmate, UncreatedClassmate
from tabulate import tabulate


# --- Constants ---
invalid_command_message = "Invalid command."
help_message = (
    "1 - Add another classmate to the database.\n"
    "2 - Remove a classmate from the database.\n"
    "3 - Edit a classmate's entry.\n"
    "4 - Search for a classmate.\n"
    "5 - View all classmates.\n"
    "6 - Calculate statistics.\n"
    "7 - Quit program."
)
quit_message = "Closing program."
failure_id_message = "Provided ID doesn't exist:"
classmate_header = ["ID", "Name", "Out of State", "Occupation", "Went to University", "University Name"]
empty_db_message = "No entries found in the database."


# --- Core Interface Functions ---
def command_input():
    """Prompt the user for a command and return the input string."""
    return input("\nCommand: ")


def help():
    """Display the list of available user commands."""
    print(help_message)


def quit():
    """Print a message confirming the program is exiting."""
    print(quit_message)


def invalid_command():
    """Print an error message for an unrecognized command."""
    print(invalid_command_message)


def successfully_action(classmate: Classmate, action: str):
    """Print a message confirming a successful database action (e.g., add, remove, edit)."""
    print(f"Successfully {action} entry:", classmate.name)


def failure_id(id: int):
    """Print a message when a given ID is not found in the database."""
    print(failure_id_message, id)


def new_data() -> UncreatedClassmate:
    """"Prompt the user for all data required to create or update a classmate entry."""
    name = input("Enter full name: ")
    out_of_state = input("Did they leave the state? (y/n): ").lower() == 'y'
    occupation = input("Enter occupation: ").lower()
    went_to_university = input("Did they go to university? (y/n): ").lower() == 'y'
    university_name = "N/A"
    if went_to_university:
        university_name = input("Enter the name of the university: ")

    return UncreatedClassmate(name, out_of_state, occupation, went_to_university, university_name)


def request_id(action: str = "access") -> int:
    """Prompt the user for a classmate ID for a given action (e.g., remove, edit)."""
    wanted_id = input(f"Enter the ID number of the classmate to {action}: ")
    while not wanted_id.isnumeric():
        invalid_command()
        wanted_id = input(f"Enter the ID number of the classmate to {action}: ")
    return int(wanted_id)


def request_name() -> str:
    """Prompt the user for a name (or partial name) to search in the database."""
    return input("Enter the name of the classmate to search: ")


# --- Output Functions ---
def print_table(data: list[Classmate]):
    """Print a list of Classmate objects in table format using tabulate."""
    if data:
        print(tabulate(data, headers=classmate_header, tablefmt="github"))
    else:
        print(empty_db_message)


def print_stats(data: dict):
    """Display calculated statistics in multiple formatted tables (university, location, top schools)."""
    # University attendance
    uni_header = ["", "Attended University", "Did Not Attend"]
    print("\n" + tabulate(data["uni_data"], headers=uni_header, tablefmt="github"))

    # State relocation
    state_header = ["", "Left the State", "Stayed in State"]
    print("\n" + tabulate(data["state_data"], headers=state_header, tablefmt="github"))

    # Top universities
    top_uni_header = ["University", "Number of Classmates"]
    print("\n" + tabulate(data["top_unis"], headers=top_uni_header, tablefmt="github"))
