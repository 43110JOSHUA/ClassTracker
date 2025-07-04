# This module contains the class for your classmates

class Classmate:
    count = 0 # Student ID

    def __init__(self, name: str, out_of_state: bool, occupation: str, went_to_university: bool, university_name: str = ""):
        self.student_id = self.count
        self.name = name
        self.out_of_state = out_of_state
        self.occupation = occupation
        self.went_to_university = went_to_university
        self.university_name = university_name