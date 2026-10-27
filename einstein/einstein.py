# CS50P Week 0 - Einsteins Equation
# This program calculates the energy equivalent of a given mass
# using Einstein's equation E=mc^2.
# The program prompts the user for the mass in kilograms
# and returns the energy equivalent in joules.

def main():
    masse = int(input("m: "))
    print(f"E:{energy(masse)}")


def energy(masse):
    """
    Calculate the energy equivalent of a given
    mass using Einstein's equation E=mc^2.
    :param masse: The mass in kilograms.
    :return: The energy equivalent in joules.
    """
    return masse * 300000000 ** 2
    # 300000000 is the speed of light in meters per second (m/s).


main()
# The code above is a simple program that takes
# user input for mass in kilograms
# and calculates the energy equivalent using Einstein's equation E=mc^2.
# The output is in joules.
