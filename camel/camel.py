# CS50P Week 2
# camelCase to snake_case converter
# This program takes a string in camelCase format and converts it to
# snake_case format.
# It does this by iterating through each character in the string and
# checking if it is uppercase. If it is, it adds an underscore before
# the character and converts it to lowercase.
# The program then returns the modified string.

def main() -> None:
    name = input("camelCase: ")
    print("snake_case:", camelCase(name))


def camelCase(name: str) -> str:
    for i in range(len(name)):
        if name[i] == name[i].upper():
            name = name[:i] + "_" + name[i].lower() + name[i+1:]
        else:
            name = name
    return name


if __name__ == "__main__":
    main()
