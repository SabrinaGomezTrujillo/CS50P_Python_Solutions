from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    font_list = figlet.getFonts()


    if len(sys.argv) not in [1, 3]:
        print("Invalid usage")
        sys.exit(1)
    elif len(sys.argv) == 1:
        x = input("Input: ")
        random_font = random.choice(font_list)
        figlet.setFont(font=random_font)
        print(figlet.renderText(x))
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f","--font"] or sys.argv[2] not in font_list:
            print("Invalid usage")
            sys.exit(1)
        else:
            x = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(x))

main()

