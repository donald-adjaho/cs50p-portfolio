# CS50P Week 2 - Fruit Calories Lookup Program
# This program prompts the user to input the name of a fruit
# (case-insensitively)
# and outputs the number of calories in one portion of that fruit,
# based on the FDA’s list of the 20 most frequently consumed raw fruits.


def main() -> None:
    # Prompt the user for a fruit name (case-insensitive input)
    fruit = str(input("Item: "))
    if output_calories(fruit):
        print(f"Calories: {output_calories(fruit)}")


# Dictionary mapping fruit names (as written in the FDA poster)
# to calorie values
nutrition_fact = {"Apple": 130, "Avocado": 50, "Banana": 110, "Cantaloupe": 50,
                  "Grapefruit": 60, "Grapes": 90, "Honeydew Melon": 50,
                  "Kiwifruit": 90, "Lemon": 15, "Lime": 20,
                  "Nectarine": 60, "Orange": 80, "Peach": 60, "Pear": 100,
                  "Pineapple": 50, "Plums": 70, "Strawberries": 50,
                  "Sweet Cherries": 100, "Tangerine": 50, "Watermelon": 80}


def output_calories(name: str) -> int | None:
    # Capitalize the first letter of the input to match the dictionary keys
    # Return the number of calories if the fruit is in the list, otherwise None
    if name.title() in nutrition_fact:
        return nutrition_fact[name.title()]


# Ensure that main is called only when this file is executed directly
if __name__ == "__main__":
    main()
