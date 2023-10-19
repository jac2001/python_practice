import sys
from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()
    
    #Check for command line arguments
    if len(sys.argv) == 1:
        #Choose a random font
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Error: Invalid font name!")
        figlet.setFont(font = font)
    else:
        sys.exit("Usage: figlet.py [-f font_name]")
    
    text = input("Enter the Text: ")
    print(figlet.renderText(text))
    
if __name__ == "__main__":
    main()