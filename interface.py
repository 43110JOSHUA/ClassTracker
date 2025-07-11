# This module contains user interface functions handling I/O

from classmate import Classmate, UncreatedClassmate
from tabulate import tabulate


invalid_command_message = "Invalid command."
help_message = ("1 - Add another classmate to the database.\n"
                "2 - Remove a classmate from the database.\n"
                "3 - Edit a classmate's entry.\n"
                "4 - Search for a classmate.\n"
                "5 - View all classmates.\n"
                "6 - Calculate statistics.\n"
                "7 - Quit program.")
quit_message = "Closing program."
failure_id_message = "Provided ID doesn't exist:"
classmate_header = ["ID", "Name", "Out of State", "Occupation", "Went to University", "University Name"]
empty_db_message = "No entries found in the database."

def command_input():
    return input("\nCommand: ")


def invalid_command():
    print(invalid_command_message)


def help():
    print(help_message)


def quit():
    print(quit_message)


def new_data() -> UncreatedClassmate:
    """This function will collect the data for the new classmate."""
    name = input("Enter full name: ")
    out_of_state = input("Did they leave the state? (y/n): ").lower() == 'y'
    occupation = input("Enter occupation: ").lower()
    went_to_university = input("Did they go to university? (y/n): ").lower() == 'y'
    university_name = "N/A"
    if went_to_university:
        university_name = input("Enter the name of the university: ")

    return UncreatedClassmate(name, out_of_state, occupation, went_to_university, university_name)


def successfully_action(classmate: Classmate, action: str):
    """This function is called for any successful operation on an entry in the database."""
    print(f"Successfully {action} entry:", classmate.name)


def request_id(action: str = "access") -> int:
    """Prompts the user for an ID number with context. Accepts a custom action string to reuse for
    different commands (e.g., 'remove', 'edit')."""
    wanted_id = input(f"Enter the ID number of the classmate to {action}: ")
    while not wanted_id.isnumeric():
        invalid_command()
        wanted_id = input(f"Enter the ID number of the classmate to {action}: ")
    
    return int(wanted_id)


def failure_id(id: int):
    print(failure_id_message, id)


def request_name() -> str:
    """Prompts the use for a name to search up in the database."""
    return input("Enter the name of the classmate to search: ")


def print_table(data: list[Classmate]):
    """This function prints all provided classmates in table format."""
    if data:
        print(tabulate(data, headers=classmate_header, tablefmt="github"))
    else:
        print(empty_db_message)
