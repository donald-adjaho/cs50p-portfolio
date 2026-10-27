# CS50P Week 6
# Objectif : This Python script counts the number of lines of code in
# a specified Python file, excluding blank lines and comments.
# It performs validation checks on command-line arguments.
# Usage: python lines.py <filename.py>
# Example: python lines.py hello.py
import sys
import os


def main():
    print(loc_function())


def loc_function():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")
    else:
        counter = 0
        with open(f"{sys.argv[1]}", "r") as file:
            for line in file:
                line_stripped = line.strip()
                if line_stripped != '' and not line_stripped.startswith("#"):
                    counter += 1
        return counter


if __name__ == "__main__":
    main()
