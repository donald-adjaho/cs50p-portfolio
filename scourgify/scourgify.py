# CS50P Week 6
# Objectif : This Python script cleans and reformats CSV data by splitting
# full names into separate first and last name columns while preserving
# house information.
# Usage: python scourgify.py input.csv output.csv
# Example: python scourgify.py before.csv after.csv
# Requirements:
#   - Input file must be a valid CSV with 'name' and 'house' columns
#   - Names must be formatted as "Last, First"
#   - Output will be written to specified file with columns: first, last, house
import sys
import csv
import os


def main():
    clean_csv_data()


def clean_csv_data():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if not os.path.isfile(input_file):
        sys.exit(f"Could not read {input_file}")
    with open(input_file) as read_csv, open(output_file, "w", newline='') as write_csv:
        reader = csv.DictReader(read_csv)
        writer = csv.DictWriter(write_csv, fieldnames=[
            "first", "last", "house"])
        writer.writeheader()
        for line in reader:
            last, first = map(str.strip, line["name"].split(","))
            writer.writerow(
                {"first": first, "last": last, "house": line["house"].strip()})


if __name__ == '__main__':
    main()
