# This module contains interface messages

help_message = """1 - Add another classmate to the database.
2 - Remove a classmate from the database.
3 - Calculate statistics.
4 - Quit program.
"""

quit_message = "Closing program."


def help():
    print(help_message)

def quit():
    print(quit_message)