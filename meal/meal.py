# CS50P Week 1 - Meal CS50
# This program is a simple implementation of a meal time checker
# that prompts the user for a time and returns a message
# indicating whether it's breakfast, lunch, or dinner time.
def main():
    """
    Main function to prompt the user for a time and
    print the corresponding meal time.
    :return: None
    """
    user = input("What time is it?")
    decimal_time = convert(user)
    if 7.0 <= decimal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= decimal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= decimal_time <= 19.0:
        print("dinner time")


def convert(time):
    """
    Convert the time from 12-hour format to decimal format
    and check if it's breakfast, lunch, or dinner time.
    :param time: The time in 12-hour format.
    :return: A string indicating the meal time.
    """
    # Normalize the time by stripping whitespace
    # and splitting it into hours and minutes.
    hours, minutes = time.strip().split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
