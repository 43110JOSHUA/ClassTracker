# This module contains user interface functions

from classmate import Classmate

invalid_command_message = "Invalid command."
help_message = ("1 - Add another classmate to the database.\n"
                "2 - Remove a classmate from the database.\n"
                "3 - Edit a classmate's entry.\n"
                "4 - Search for a classmate.\n"
                "5 - View all classmates.\n"
                "6 - Calculate statistics.\n"
                "7 - Quit program.")
quit_message = "Closing program."
successful_entry_message = "Successfully added entry:"
successful_remove_message = "Successfully removed entry:"
failure_remove_message = "Provided ID doesn't exist:"

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
    print(successful_entry_message, classmate.name)


def remove_data() -> int:
    """This function will collect and return the ID number of the classmate to remove."""
    id_to_remove = input("Enter the ID number of the entry to remove: ")
    while not id_to_remove.isnumeric():
        invalid_command()
        id_to_remove = input("Enter the ID number of the entry to remove: ")
    
    return int(id_to_remove)


def successfully_removed(classmate_name: str):
    print(successful_remove_message, classmate_name)


def failure_remove(id: int):
    print(failure_remove_message, id)


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
