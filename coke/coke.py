# CS50P Week 2
# Objective: Simulate a Coke vending machine transaction
#
# Description:
#   - A Coke costs exactly 50 cents.
#   - The machine only accepts coins of 25, 10, and 5 cents.
#   - The user is repeatedly prompted to insert a coin.
#   - After each valid coin, the remaining amount due is updated and displayed.
#   - Invalid coins (not 25, 10, or 5) are ignored silently.
#   - Once the total reaches or exceeds 50 cents:
#       - If the inserted coin exactly completes 50 cents, it prints
# "Change Owed: 0".
#       - If the inserted coin exceeds the amount due, it prints the
# correct change owed.
#   - The program terminates after the Coke is fully paid.


def main() -> None:
    cokeMachine()


def cokeMachine():
    amountDue = 50
    changeOwed = 0
    print(f"Amount Due: {amountDue}")
    while amountDue > 0:
        coin = int(input("Insert coin: "))
        if coin in {25, 10, 5}:
            if coin > amountDue:
                print(f"Change Owed: {coin - amountDue}")
                break
            amountDue -= coin
            if amountDue == 0:
                print(f"Change Owed: {changeOwed}")
                break
            else:
                print(f"Amount Due: {amountDue}")
        else:
            print(f"Amount Due: {amountDue}")


if __name__ == '__main__':
    main()
