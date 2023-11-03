import random
from art import logo

print(logo)


def level_of_game():
    lv = input("Choose a difficulty. Type 'easy' or 'hard':")
    steps = 0
    if lv == 'easy':
        steps = 10
    elif lv == 'hard':
        steps = 5
    return steps


def compare(guess_number, step_number):
    if step_number == 1 and COMP_NUMB != guess_number:
        print("You've run out of guesses, you lose.")
        return 0
    if COMP_NUMB == guess_number:
        print(f"You got it! The answer was {COMP_NUMB}.")
        return 0
    elif guess_number < COMP_NUMB:
        print("Too low.")
        step_number = step_number - 1
        return step_number
    elif guess_number > COMP_NUMB:
        print("Too high.")
        step_number = step_number - 1
        return step_number


def game():
    global COMP_NUMB
    COMP_NUMB = random.randint(0, 100)
    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
    """)
    print(COMP_NUMB)
    step = level_of_game()
    while step != 0:
        print(f"You have {step} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        step = compare(guess, step)
        print("Guess again")


game()
