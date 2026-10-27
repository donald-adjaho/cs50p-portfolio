# CS50P Week 2 - Plate Validation Program
# Checks if a license plate is valid based on specific rules
# Rules:
#   - Plates must start with at least two letters
#   - Plates must be between 2 and 6 characters long
#   - Plates may contain only alphanumeric characters
# (no spaces or punctuation)
#   - Numbers, if present, must appear only at the end
#   - The first number cannot be a '0'
#
# The program prompts the user for a plate input, then prints "Valid"
# or "Invalid"
# depending on whether the plate meets all the criteria.


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    # True if the string is alphanumeric and contains at least one letter and
    # one digit
    v_al = s.isalnum() and any(x.isalpha()
                               for x in s) and any(x.isdigit() for x in s)
    # True if the string contains only letters
    v_di = s.isalpha()
    # Apply all validation checks for plates with both letters and digits
    if v_al:
        return comb_valid1(s) and comb_valid2(s) and valid_number(s) and numbers_at_end(s)
    # Apply basic checks for plates with letters only
    if v_di:
        return max_len(s) and unaccepted_character(s)
    else:
        return False

# Group of structural validations


def comb_valid1(s: str):
    return max_len(s) and valid_characters(s)

# Group of digit-related and special character checks


def comb_valid2(s: str):
    return count_number(s) and unaccepted_character(s)

# Checks if the plate is less than 7 characters long


def max_len(s):
    return 2 < len(s) < 7

# Checks that the first two characters are letters
# and all characters are alphanumeric


def valid_characters(s: str):
    if not s[:2].isalpha():
        return False
    for i in range(len(s)):
        if not s[i].isalnum():
            return False
    return True

# Checks if the last character is a digit


def valid_number(s: str):
    return s[-1].isnumeric()

# Ensures that the first digit in the plate (if any) is not 0


def count_number(s: str):
    count = 0
    indice = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            count += 1
            if count == 1:
                indice = i
    if count == 0:
        return False
    return int(s[indice]) != 0

# Ensures no forbidden characters are present


def unaccepted_character(s: str):
    outside_character = set(" !,.:?;")
    for i in s:
        if i in outside_character:
            return False
    else:
        return True


# Check if a letter sit after digit in plate given


def numbers_at_end(s: str) -> bool:
    number_started = False
    for car in s:
        if car.isdigit():
            number_started = True
        elif number_started and car.isalpha():
            return False
    return True


if __name__ == "__main__":
    main()
