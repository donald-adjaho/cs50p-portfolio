# CS50P Week8
# Objective: Create personalized CS50 completion
# certificates with t-shirt image
# Features:
#   - Generates PDF with custom name overlay
#   - Uses predefined shirt image template
#   - Centered text and image placement
# Usage:
#   - Prompt: "Name: " (user inputs their name)
#   - Output: "shirtificate.pdf" saved in current directory
# Requirements:
#   - background.png (A4 background image)
#   - shirtificate.png (shirt image)
#   - fpdf2 package installed
# Customization:
#   - Font: Helvetica (40pt for title, 20pt for name)
#   - Text color: White
#   - Image positioning: Centered horizontally
from fpdf import FPDF


class Shirtificate:

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_shirtificate(cls, name):
        cls.pdf = FPDF(format="A4")
        cls.pdf.add_page()
        # cls.pdf.image("./background.png", x=0, y=0, w=210, h=297)
        cls.pdf.set_font("Helvetica", size=40)
        cls.pdf.cell(w=0, h=50, text="CS50 Shirtificate",
                     markdown=True, align="c", new_y="NEXT")
        image_mm = 150
        x = (210-image_mm)/2
        cls.pdf.image("./shirtificate.png", x=x, y=60, w=image_mm)
        cls.pdf.set_text_color(255, 255, 255)
        cls.pdf.set_y(97)
        cls.pdf.set_font("Helvetica", size=20)
        cls.pdf.cell(
            w=0, h=20, text=f"{name} took CS50", markdown=True, align="c")
        cls.pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    return Shirtificate.create_shirtificate(name)


if __name__ == "__main__":
    main()
