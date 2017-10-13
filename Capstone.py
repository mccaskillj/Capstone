from sys import *
from PIL import Image
from traceTop import *
from horizontalHist import *
from verticalHist import *
from segmenter import *
import argparse


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', action="store", help='Input image name')
    parser.add_argument('-v', action='count', default=0, help='Enable verbose')
    parser.add_argument('-t', action='store', type=int, default=20, help='Threshold for vertical hist')
    results = parser.parse_args()
    try:
        Image.open(results.filename)
    except:
        print("file \"" + argv[1] + "\" not found")
        return 0

    menu(results)


def menu(results):
    val = menuItems()
    while checkChoice(val):
        print()
        val = menuItems()

    val = int(val)

    if val == 1:
        hist = VHist(results)
        hist.findBreaks(results.t)
        if results.v > 1:
            hist.showBreaks()
        print(hist.getMax())
        seg = Segmenter(hist)
        print seg.segmentNew()
    elif val == 2:
        hist = HHist(results)
        hist.showHist()
        hist.generateHeight(10)
        print(hist.getHeight())
    elif val == 3:
        top = TopTrace(results)
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