# CS50P Week 3
# This code creates a grocery list from user input, counts the occurrences
# of each item, and then prints the count followed by the uppercase item name.
# The input process continues until an EOFError is encountered (e.g., Ctrl+D
# on Unix-like systems or Ctrl+Z then Enter on Windows).

def main() -> None:
    setGroceryList()


def makeGroceryList() -> list:
    listConstructor = []
    while True:
        try:
            gelement = input()
            listConstructor.append(gelement)
        except EOFError:
            break
    return sorted(listConstructor)


def setGroceryList() -> str:
    groceryList = makeGroceryList()
    for i in dict.fromkeys(groceryList):
        print(f'{groceryList.count(i)} {str(i).upper()}')


if __name__ == "__main__":
    main()
