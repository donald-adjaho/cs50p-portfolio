# CS50P Week 4
# Guessing game implementation
# This program prompts the user to choose a difficulty level,
# then generates a random number between 1 and the chosen level.
# The user must guess the number, receiving feedback after each guess:
# - "Too small" if the guess is lower than the target,
# - "Too large" if the guess is higher than the target,
# - "Just right !" when the guess is correct.
# The program handles invalid inputs gracefully
# and repeats until the correct guess.
import random


def main():
    randomgame()


def randomgame():
    while True:
        try:
            prompt_level = int(input("Level: "))
            if prompt_level > 0:
                break
        except ValueError:
            continue
    random_choice = random.randint(1, prompt_level)
    while True:
        try:
            prompt_guess = int(input("guess: "))
            if prompt_guess < 1:
                continue
        except ValueError:
            continue
        if prompt_guess < random_choice:
            print("Too small!")
            continue
        elif prompt_guess > random_choice:
            print("Too large!")
            continue
        elif prompt_guess == random_choice:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
