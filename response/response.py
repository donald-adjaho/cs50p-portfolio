# CS50P Week7
# Objective: Check if an email address is valid using the `validators` library
# Features:
#   - Utilizes external library `validators.email()`
#   - Simple input/output interface
# Usage:
#   - Prompt: "What's your email address?"
#   - Output: "Valid" or "Invalid"
# Notes:
#   - Handles general email format validation
#   - Ignores regex or custom validation logic
import validators


def main():
    print(validate_email(input("What's your email address? ")))


def validate_email(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
