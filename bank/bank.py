# CS50P Week 1 - Bank CS50
# This program is a simple implementation of a bank system
# that greets the user and provides a reward based on their greeting.
def main() -> None:
    """
    Main function to prompt the user for a greeting and
    print the corresponding reward.
    :return: None
    """
    # Prompt the user for a greeting and strip whitespace.
    greeting = input("Greeting: ")
    print(process_gretting(greeting))


def process_gretting(greeting: str) -> str:
    """
    Process the user's greeting and return a reward based on the greeting.
    :param greeting: The user's greeting.
    :return: A string indicating the reward based on the greeting.
    """
    # Normalize the greeting by stripping whitespace, converting to lowercase,
    format_greeting = greeting.strip().lower().split()
    # Check if the greeting starts with "hello" or "h"
    # and assign a reward accordingly.
    reward = ""
    if format_greeting[0].strip(".,!:?") == "hello":
        reward = "$0"
    elif format_greeting[0][0] == "h":
        reward = "$20"
    else:
        reward = "$100"
    # Return the reward based on the greeting.
    return reward


main()
