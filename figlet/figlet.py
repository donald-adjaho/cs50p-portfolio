# CS50P Week 4
# figlet.py: A program that renders user input
# as ASCII art using the pyfiglet library.
# Usage:
#   python figlet.py -f <fontname>     → to use a specific font
#   python figlet.py                   → to use the default font
import pyfiglet
import sys
from pyfiglet import FigletFont


def main():
    figlet_input()


def figlet_input():
    prefix_font = {"-f", "--font"}
    if len(sys.argv) not in {1, 3}:
        sys.exit("Invalid Usage")
    if len(sys.argv) == 1:
        prompt_user = input("Input: ")
        print(f"{pyfiglet.figlet_format(prompt_user)}")
    else:
        if sys.argv[1] in prefix_font and sys.argv[2] in FigletFont.getFonts():
            prompt_user = input("Input: ")
            font_name = sys.argv[2]
            f = pyfiglet.figlet_format(prompt_user, font=font_name)
            print(f"Output: \n{f}")
        else:
            sys.exit("Invalid Usage")


if __name__ == "__main__":
    main()
