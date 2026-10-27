# CS50P Week 1 Interpreter
# This program is a simple implementation of a mathematical interpreter
# that takes a mathematical expression as input and returns the result.
# The program supports addition, subtraction, multiplication, and division.

def main() -> None:
    """
    Main function to prompt the user for expressions and
    print the result of the interpreter.
    :return: None
    """
    expressions = input("Expressions: ")
    result = interpreter(expressions)
    print(result)


def interpreter(expressions) -> float:
    """
    Function to interpret a mathematical expression and return the result.
    :param expressions: The mathematical expression as a string.
    :return: The result of the expression as a float.
    """
    # Normalize the expression by stripping whitespace
    # and splitting it into parts.
    expressions = expressions.strip(".,!:;?")
    parts = expressions.split()
    if len(parts) == 3:
        x, y, z = parts
        if y == "+":
            return (round(float(x) + float(z), 1))
        elif y == "-":
            return (round(float(x) - float(z), 1))
        elif y == "*":
            return (round(float(x) * float(z), 1))
        elif y == "/":
            return (round(float(x) / float(z), 1))
    else:
        return ("Invalid expression")


if __name__ == "__main__":
    main()
