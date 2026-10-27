# CS50P Week6
# Objectif : This Python script reads a CSV file containing pizza
# orders and displays the data in a formatted table using the tabulate library.
# Usage: python pizza.py <filename.csv>
# Example: python pizza.py regular.csv
# Requirements:
#   - CSV file must have exactly 3 columns
#   - File must exist and be a valid CSV
#   - First row must contain column headers
import os
import sys
from tabulate import tabulate
import csv


def main():
    print(pizza_table())


def pizza_table():
    f_list = []
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    if not os.path.isfile(f"{sys.argv[1]}"):
        sys.exit("File does not exist")
    with open(f"{sys.argv[1]}", "r") as csv_file:
        f = csv.DictReader(csv_file)
        header = f.fieldnames
        if header is None:
            raise ValueError("No header found in csv file")
        for i in f:
            f_list.append([i[header[0]], i[header[1]], i[header[2]]])
    return (tabulate(f_list, header, tablefmt="grid"))


if __name__ == "__main__":
    main()
