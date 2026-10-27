# CS50P Week7
# Objective: Count the number of standalone "um" occurrences in text
# Features:
#   - Uses regex with word boundary rules
#   - Case-insensitive
#   - Ignores "um" as part of other words like "lump", "umbrella"
# Usage:
#   - Prompt: "Text: "
#   - Output: Number of "um" words found
# Notes:
#   - Pattern: (?<!\w)um(?!\w) ensures strict matching
import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"(?<!\w)um(?!\w)"
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
