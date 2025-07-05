# This module contains user interface functions

from classmate import Classmate

invalid_command_message = "Invalid command."
help_message = """1 - Add another classmate to the database.
2 - Remove a classmate from the database.
3 - Edit a classmate's entry.
4 - Search for a classmate
5 - Calculate statistics.
6 - Quit program."""
quit_message = "Closing program."
successful_entry = "Successfully added entry:"

def invalid_command():
    print(invalid_command_message)


def help():
    print(help_message)


def quit():
    print(quit_message)


def new_data() -> Classmate:
    """This function will collect and create the new classmate."""
    correct = False
    while not correct:
        new_classmate = _get_new_data()
        correct = _validate_new_data(new_classmate)

    return new_classmate


def successfully_added(classmate: Classmate):
    print(successful_entry, classmate.name)


# HELPERS
def _get_new_data() -> Classmate:
    """This helper function is used to collect the information of the new classmate."""
    name = input("Enter full name: ")
    out_of_state = input("Did they leave the state? (y/n): ").lower() == 'y'
    occupation = input("Enter occupation: ").lower()
    went_to_university = input("Did they go to university? (y/n): ").lower() == 'y'
    university_name = "N/A"
    if went_to_university:
        university_name = input("Enter the name of the university: ").lower()

    return Classmate(name, out_of_state, occupation, went_to_university, university_name)


def _validate_new_data(new_classmate: Classmate) -> bool:
    """This helper function prints the collected information so the user can double check if it's correct."""
    print("\nSUMMARY:")
    print(new_classmate)

    return input("Is the following information correct? (y/n): ") == 'y'
