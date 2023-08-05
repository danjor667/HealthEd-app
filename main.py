i#!/usr/bin/python3
"""
main function
"""
def load_quiz_data(filename):
    with open(filename, "r") as file:
        quiz_data = eval(file.read())
    return quiz_data
def display_categories(quiz_data):
    print("Select a category:")
    for index, category in enumerate(quiz_data.keys(), start=1):
        print(f"{index}. {category}")
