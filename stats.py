# This module handles the calculation of statistics

from classmate import Classmate
from collections import Counter


def compute_stats(classmates: list[Classmate]) -> dict:
    """This function takes in a list of Classmates in the database and computes the number 
    of students who went to university, who left the state, and the top 3 universities. Returns a dictionary
    of the data."""
    if not classmates:
        return None

    total = len(classmates)

    # Uni stats
    uni_classmates = [c for c in classmates if c.went_to_university]
    to_uni = len(uni_classmates)
    percent_to_uni = str(round(to_uni / total, 2) * 100) + "%"
    no_uni = total - to_uni
    percent_no_uni = str(round(no_uni / total, 2) * 100) + "%"
    uni_data = [("Count", to_uni, no_uni), ("Percent", percent_to_uni, percent_no_uni)]

    # State stats
    out_state = len([c for c in classmates if c.out_of_state])
    percent_out = str(round(out_state / total, 2) * 100) + "%"
    in_state = total - out_state
    percent_in = str(round(in_state / total, 2) * 100) + "%"

    state_data = [("Count", out_state, in_state), ("Percent", percent_out, percent_in)]

    # Top unis
    number_of_common_unis = 3
    top_unis = Counter(c.university_name for c in uni_classmates).most_common(number_of_common_unis)
    
    return {"total": total, "uni_data": uni_data, "state_data": state_data, "top_unis": top_unis}