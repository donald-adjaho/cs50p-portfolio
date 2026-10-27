# CS50P Week 2 - Text Shortener (Twitter Style)
#
# This program prompts the user to enter a string of text.
# It returns the same text with all vowels (A, E, I, O, U) removed,
# regardless of whether they are uppercase or lowercase.
#
# This mimics the way some words are shortened in tweets or text messages,
# similar to how "Twitter" was once written as "twttr".


def main() -> None:
    insert = str(input("Input: "))
    print(omittingVowels(insert))


def omittingVowels(insert: str) -> str:
    vowels = set("aeiouAEIOU")
    return f"Output: {''.join([i for i in insert if i not in vowels])}"


if __name__ == "__main__":
    main()
