# This module contains the class to represent your classmates
from collections import namedtuple

# for no_ID classmate
UncreatedClassmate = namedtuple("UncreatedClassmate", ["name", "out_of_state", "occupation", "went_to_university", "university_name"])

class Classmate:
    def __init__(self, id: int, name: str, out_of_state: bool, occupation: str, went_to_university: bool, university_name: str):
        self.id = id
        self.name = name
        self.out_of_state = out_of_state
        self.occupation = occupation
        self.went_to_university = went_to_university
        self.university_name = university_name


    def __str__(self):
        return (f"Name: {self.name}\nOut of state: {self.out_of_state}\nOccupation: {self.occupation}\n"
                f"Went to university: {self.went_to_university}\nUniversity name: {self.university_name}")