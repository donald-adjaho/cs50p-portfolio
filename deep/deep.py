# CS50P Week 1 - Deep CS50
# This program is a simple implementation of the Deep Thought computer

def main() -> None:
    """
    Main function to prompt the user for input and
    check if the answer is correct.
    :return: None
    """
    user = input(
        """What is the Answer to the Great Question of Life,the Universe,
        and Everything?""").strip().lower()
    output = deep_thought(user)
    print(output)


def deep_thought(x) -> str:
    """
    Function to check if the user's answer is correct.
    :param x: User's input.
    :return: A string indicating whether the answer is correct or not.
    """
    if x in ['42', 'forty-two', 'forty two', 'Forty-two']:
        response = "Yes"
    else:
        response = "No"
    return response


main()
