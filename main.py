#!/usr/bin/python3
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
def select_category(quiz_data):
    while True:
        choice = int(input("Enter the category number: "))
        if choice in range(1, len(quiz_data) + 1):
            categories = list(quiz_data.keys())
            selected_category = categories[choice - 1]
            return selected_category
        else:
            print("Invalid category number. Please try again.")
def get_random_question(quiz_data, category):
    questions = quiz_data[category]
    return random.choice(questions)
