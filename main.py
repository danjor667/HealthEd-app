#!/usr/bin/python3
"""
main
"""

import random

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

def present_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)

def get_user_answer():
    while True:
        user_answer = input("Enter your answer (A, B, C, or D), or type 'exit' to quit: ").upper()
        if user_answer in ["A", "B", "C", "D", "EXIT"]:
            return user_answer
        else:
            print("Invalid answer. Please choose A, B, C, or D.")

def check_answer(question, user_answer):
    correct_answer = question["answer"]
    if user_answer == correct_answer:
        print("Correct answer!")
    else:
        print("\nIncorrect answer. The correct answer is", correct_answer)

def play_quiz_game(quiz_data):
    print("\n\n\t\t--------------Welcome to the Health Education Quiz Game!----------------")
    display_categories(quiz_data)

    selected_category = select_category(quiz_data)
    print(f"\n\t\tYou have selected the '{selected_category}' category.\n")

    question = get_random_question(quiz_data, selected_category)
    present_question(question)

    user_answer = get_user_answer()
    if user_answer == "EXIT":
        print("Exiting the program...")
        return
    check_answer(question, user_answer)

quiz_data = load_quiz_data("quiz_questions.txt")

while True:
    play_quiz_game(quiz_data)
    continue_playing = input("\nDo you want to play again? type (y) for yes, any other key to quit: \n")
    if continue_playing.lower() != "y":
        print("Exiting the program...")
        break

