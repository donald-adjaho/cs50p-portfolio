# CS50P Week 6
# Objectif : This program creates customized CS50 shirt
# certificates by overlaying a shirt image on student
# photos while maintaining proper sizing.
# Usage: python shirt.py input.jpg output.jpg
# Example: python shirt.py before.jpg after.png
# Requirements:
#   - Input must be JPG/PNG image file
#   - Output must have same extension as input
#   - 'shirt.png' must exist in working directory
#   - Images will be resized to 600x600 pixels before processing
import os
import sys
from PIL import Image, ImageOps


def main():
    took_cs50()


def took_cs50():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    valid_extensions = (".png", ".jpg", ".jpeg")
    if not input_file.endswith(valid_extensions):
        sys.exit("Invalid input")
    if not output_file.endswith(valid_extensions):
        sys.exit("Invalid output")
    if input_file.split(".")[1] != output_file.split(".")[1]:
        sys.exit("Input and output have different extensions")
    if not os.path.isfile(sys.argv[1]):
        sys.exit("Input does not exist")
    with Image.open(f"{input_file}", "r") as file_img, Image.open("shirt.png", "r") as overlay_img:
        transform_file = ImageOps.fit(file_img, (600, 600))
        transform_file.paste(overlay_img, (0, 0), overlay_img)
        transform_file.save(output_file)


if __name__ == "__main__":
    main()
