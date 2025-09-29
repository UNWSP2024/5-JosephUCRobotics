# Author: Joseph Kracht
# Last Modified: 9/26/2025
# Title: Math Quiz

# Program #2: Math Quiz


import random


def display_quiz(number_1, number_2):
    print("What is")
    print(f'{number_1:5}')
    print(f'+{number_2:4}')
    print('-----')

def display_answer(user_input, answer):
    if user_input == answer:
        print("Correct!")
    else:
        print("Wrong. The correct answer is",answer)

# Pick random numbers
random_number_1 = random.randint(1, 999)
random_number_2 = random.randint(1, 999)

# Get answer
correct_answer = random_number_1 + random_number_2

# Display quiz
display_quiz(random_number_1, random_number_2)

# Get input
user_answer = int(input())

# Display answer
display_answer(user_answer, correct_answer)
