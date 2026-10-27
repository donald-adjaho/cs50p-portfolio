# CS50P Week 4
# adieu.py program implementation
# This program collects multiple names from the user until an EOF is
# encountered,
# and then prints a farewell message in the style of "So Long,
# Farewell" from The Sound of Music.

def main():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            if name:
                names.append(name)
        except EOFError:
            break

    if names:
        print(f"\nAdieu, adieu, to {format_names(names)}")


def format_names(names):
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return f"{', '.join(names[:-1])}, and {names[-1]}"


if __name__ == "__main__":
    main()
