# This module contains the class to represent your classmates

class Classmate:
    count = 0 # Classmate ID

    def __init__(self, name: str, out_of_state: bool, occupation: str, went_to_university: bool, university_name: str):
        self.classmate_id = self.count
        self.name = name
        self.out_of_state = out_of_state
        self.occupation = occupation
        self.went_to_university = went_to_university
        self.university_name = university_name


    def __str__(self):
        return (f"Name: {self.name}\nOut of state: {self.out_of_state}\nOccupation: {self.occupation}\n"
                f"Went to university: {self.went_to_university}\nUniversity name: {self.university_name}")