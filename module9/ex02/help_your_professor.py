#!/usr/bin/python3

# key = naam van de student
# value = cijfer van de opdracht

def average(scores_dictionary):
    grades = list(scores_dictionary.values())
    average_grades = sum(grades) / len(grades)
    
    return average_grades


class_3B = {
    "marine" : 18,
    "jean" : 15,
    "coline" : 8,
    "luc" : 9
}

class_3C = {
    "quentin" : 17,
    "julie" : 15,
    "marc" : 8,
    "stephanie" : 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")