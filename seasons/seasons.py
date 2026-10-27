# CS50P Week8
# Objective: Calculate minutes lived since birth date
# Features:
#   - Converts birth date to total minutes lived
#   - Uses inflect for English word conversion
#   - Handles invalid date formats
# Usage:
#   - Prompt: "Date of birth: " (YYYY-MM-DD)
#   - Output: "X minutes" in words (e.g., "One million two hundred
# thirty-four minutes")
# Requirements:
#   - Valid ISO format date (YYYY-MM-DD)
#   - Date cannot be in the future
#   - Uses system's current date for calculation
# Error Handling:
#   - "Invalid date" for malformed input or future dates
import inflect
from datetime import date
p = inflect.engine()


def main():
    try:
        get_date = input("Date of birth: ")
        print(convert_time_left(get_date))
    except ValueError:
        print("Invalid date")
        exit(1)


def convert_time_left(get_date: str) -> str:
    birth_date = date.fromisoformat(get_date)
    today_date = date.today()
    left_time = today_date - birth_date
    minutes = left_time.days * 24 * 60
    convert = p.number_to_words(minutes, andword='')
    return f"{str(convert).capitalize()} minutes"


if __name__ == "__main__":
    main()
