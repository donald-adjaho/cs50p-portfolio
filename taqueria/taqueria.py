# CS50P Week 3
# This code simulates a taqueria ordering process.
# It takes item names as input,
# calculates the running total of the order based on a predefined menu,
# and displays the updated total after each valid item. The process ends
# when an empty input is provided.

def main() -> None:
    taqueriaProcess()


taqueria_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def taqueriaProcess() -> float:
    total = 0.0
    while True:
        try:
            item = input("Item: ").title()
            if item in taqueria_dict:
                total = taqueria_dict[item] + total
                print(f'Total: ${total:.2f}')
        except EOFError:
            break


if __name__ == '__main__':
    main()
