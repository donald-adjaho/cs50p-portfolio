# CS50P Week7
# Objective: Convert time ranges from 12-hour format to 24-hour format
# Features:
#   - Accepts input like "9 AM to 5 PM" or "9:30 AM to 5:45 PM"
#   - Validates input using regular expressions
#   - Handles optional minutes
#   - Raises ValueError on invalid format
# Usage:
#   - Prompt: "Hours: "
#   - Output: "09:00 to 17:00" (24-hour format)
# Notes:
#   - Uses dictionaries to map AM/PM hours to 24-hour equivalents
#   - Handles inputs with or without minutes
import re


def main():
    print(convert(input("Hours: ")))


def convert(s: str):
    am_dict = {"12": "00", "1": "01", "2": "02",
               "3": "03", "4": "04", "5": "05", "6": "06",
               "7": "07", "8": "08", "9": "09", "10": "10", "11": "11"}
    pm_dict = {"12": "12", "1": "13", "2": "14",
               "3": "15", "4": "16", "5": "17", "6": "18",
               "7": "19", "8": "20", "9": "21", "10": "22", "11": "23"}
    pattern = r"""^(1[0-2]|[1-9])(?::([0-5]\d))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5]\d))? (AM|PM)$"""
    matches = re.fullmatch(pattern, s.strip())
    if matches:
        group1 = matches.group(1)
        group2 = matches.group(2)
        group3 = matches.group(3)
        group4 = matches.group(4)
        group5 = matches.group(5)
        group6 = matches.group(6)
        hours1, hours2 = "", ""
        minutes1, minutes2 = "", ""
        if group3 == "AM":
            hours1 = am_dict[group1]
        elif group3 == "PM":
            hours1 = pm_dict[group1]
        if group6 == "AM":
            hours2 = am_dict[group4]
        elif group6 == "PM":
            hours2 = pm_dict[group4]
        if not group2:
            minutes1 = "00"
        else:
            minutes1 = group2
        if not group5:
            minutes2 = "00"
        else:
            minutes2 = group5
        return f"{hours1}:{minutes1} to {hours2}:{minutes2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
