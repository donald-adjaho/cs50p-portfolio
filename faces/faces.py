# CS50P Week 0 - Faces.py
# This program takes user input and replaces ":(" with "🙁" and ":)" with "🙂".

def convert(something: str) -> str:
    """
    Convert the input string by replacing spaces with
    ellipses and converting to lowercase.
    :param something: The input string to be converted.
    :return: The converted string.
    """

    something = something.replace(":(", "🙁")
    something = something.replace(":)", "🙂")
    return something


def main() -> None:
    """
    Main function to take user input and convert it.
    """
    sentence = input()
    print(convert(sentence))


main()
