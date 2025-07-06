# This module contains the class to represent your classmates
from collections import namedtuple

# for no_ID classmate. Used when adding and updating entries
UncreatedClassmate = namedtuple("UncreatedClassmate", ["name", "out_of_state", "occupation", "went_to_university", "university_name"])

class Classmate:
    def __init__(self, id: int, name: str, out_of_state: bool, occupation: str, went_to_university: bool, university_name: str):
        self.id = id
        self.name = name
        self.out_of_state = out_of_state
        self.occupation = occupation
        self.went_to_university = went_to_university
        self.university_name = university_name


    def to_list(self):
        """This method returns all the classmate's data in a list for printing"""
        return [self.id, self.name, self.out_of_state, self.occupation, self.went_to_university, self.university_name]