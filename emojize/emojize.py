# CS50P Week 4
# This program takes user input and converts emoji codes (like :smile:)
# into actual emojis.
import emoji


def main() -> None:
    print(f_emojizer())


def f_emojizer():
    prompt = input("input: ")
    output = emoji.emojize(prompt, language="alias")
    return f"output: {output}"


if __name__ == "__main__":
    main()
