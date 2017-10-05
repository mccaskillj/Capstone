from sys import *
from PIL import Image
from traceTop import *
from horizontalHist import *
from verticalHist import *


def main(argv):
    if len(argv) != 2:
        print("usage:",argv[0], "filename")
        return 0;
    try:
        Image.open(argv[1])
    except:
        print("file \"" + argv[1] + "\" not found")
        return 0

    menu()


def menu():
    val = menuItems()
    while checkChoice(val):
        print()
        val = menuItems()

    val = int(val)

    if val == 1:
        verticalHist(argv[1])
    elif val == 2:
        horizontalHist(argv[1])
    elif val == 3:
        traceTop(argv[1])
    else:
        return 0


def menuItems():
    print("Please Select One of the Following:")
    print("\t1) Vertical Hist")
    print("\t2) Horizontal Hist")
    print("\t3) Trace Top")
    return str(input("Choice: "))

def checkChoice(userVal):
    if not userVal.isdigit():
        return True
    else:
        val = int(userVal)
        if 0 >= val > 3:
            return True

    return False

main(argv)