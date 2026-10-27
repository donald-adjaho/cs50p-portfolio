# CS50P Week 0 - Playback.py
# This program takes user input and replaces spaces with ellipses.
# The ellipses are represented by three dots (...).

def main():
    sentence = input("Say something: ")
    print(playback(sentence))


def playback(something):
    return something.replace(" ", "...")


main()
# The code above is a simple program that takes
# user input and replaces spaces with ellipses.
