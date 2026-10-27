# CS50P Week 4
# This program implements a math quiz game,
# that tests the user's ability to solve
# 10 addition problems based on the selected difficulty level.
# - Level 1: easy (numbers between 0 and 1000)
# - Level 2: medium (numbers between 0 and 10000)
# - Level 3: hard (numbers between 0 and 100000)
# For each problem, the user has up to 3 attempts to input the correct result.
# An incorrect answer or invalid
# input (e.g., non-numeric) results in an "EEE" message.
# If the user fails all 3 attempts, the correct answer is displayed.
# At the end, the program prints the user's final score.
import random


def main():
    level = get_level()
    count_problems = 0
    failure_score = 0
    while count_problems < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        retry_guess = 0
        while retry_guess < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                retry_guess += 1
                continue
            result = x + y
            if guess == result:
                break
            else:
                print("EEE")
                retry_guess += 1
        if retry_guess == 3:
            print(f"{x} + {y} = {x + y}")
            failure_score += 1
        count_problems += 1
    print(f"Score: {count_problems - failure_score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in {1, 2, 3}:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
