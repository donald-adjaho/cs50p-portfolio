# CS50P Week 3
# This code takes a date input from the user in one of two formats
# ("Month Day, Year" or "Day/Month/Year") and converts it to the
# "YYYY-MM-DD" format. It continues to prompt the user for a date
# until a valid format is provided.
from datetime import datetime


def main():
    print(convertDate())


def convertDate():
    while True:
        date = input("Date: ").strip()
        for fmt in ("%B %d, %Y", "%m/%d/%Y"):
            try:
                date_obj = datetime.strptime(date, fmt)
                return date_obj.strftime("%Y-%m-%d")
            except ValueError:
                continue


if __name__ == "__main__":
    main()
