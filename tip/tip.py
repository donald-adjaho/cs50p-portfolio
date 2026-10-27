# CS50P Week 0 - Tip.py
# This program calculates the tip amount based on user input.
# It prompts the user for the meal cost and tip percentage,

def main():
    """
    Main function to calculate the tip based on user input.
    It prompts the user for the meal cost and tip percentage,
    calculates the tip amount, and prints the result.
    :return: None
    """
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    """
    Convert a string representing a dollar amount to a float.
    :param d: The dollar amount as a string (e.g., "$10.00").
    :return: The dollar amount as a float (e.g., 10.00).
    """
    d = float(d.strip("$"))
    return d


def percent_to_float(p: int) -> float:
    """
    Convert a string representing a percentage to a float.
    :param p: The percentage as a string (e.g., "15%").
    :return: The percentage as a float (e.g., 0.15).
    """
    p = float(p.strip("%")) / 100
    return p


main()
