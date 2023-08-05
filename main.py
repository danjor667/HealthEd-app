i#!/usr/bin/python3
"""
main function
"""
def load_quiz_data(filename):
    with open(filename, "r") as file:
        quiz_data = eval(file.read())
    return quiz_data
