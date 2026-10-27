# CS50P Week 3
# This code defines functions to get a valid fuel fraction from the user,
# calculate the percentage, and display the fuel level as "E" (Empty),
# "F" (Full), or a percentage value.

def main() -> None:
    print(setGauge())


def fuelGauge():
    while True:
        try:
            entry = input("Fraction: ")
            first, second = entry.split("/")
            x = int(first)
            y = int(second)
            if x > y:
                continue
            if y == 0:
                continue
            return x, y
        except ValueError:
            pass


def setGauge():
    x, y = fuelGauge()
    operating = round((x/y)*100)
    if operating <= 1:
        value = "E"
    elif operating >= 99:
        value = "F"
    else:
        value = f"{operating}%"
    return value


main()
