from sys import *
from PIL import Image
from traceTop import *
from horizontalHist import *
from verticalHist import *
from segmenter import *
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', action="store", help='Input image name')
    parser.add_argument('-v', action='count', default=0, help='Enable verbose')
    parser.add_argument('-t', action='store', type=int, default=20, help='Threshold for vertical hist')
    parser.add_argument('-l', action='store', type=float, default=1.5, help='low weight for top trace')
    parser.add_argument('-y', action='store', type=float, default=0.5, help='high weight of top trace')
    parser.add_argument('-z', action='store', type=float, default=50, help='threshold for top trace (%)')
    parser.add_argument('-s', action='count', default=0, help='Segment the image')
    parser.add_argument('-g', action='count', default=0, help='Remove gaps (thinning algorithm)')
    parser.add_argument('-x', action='store', type=int, default=0, help='Override for testing')
    results = parser.parse_args()
    try:
        Image.open(results.filename)
    except:
        print("file \"" + argv[1] + "\" not found")
        return 0
    if results.x == 0:

        user = input("How many characters are in the image? ")

        try:
            user = int(user) + 1
        except:
            print("Invalid character count")
            return

        val = menuItems()
        while checkChoice(val):
            print()
            val = menuItems()

        val = int(val)

        vert, top = menu(results, val)
    else:
        vert, top = menu(results, 5)
        user = results.x + 1

    testingOutput(user, argv[1], vert, top)


def menu(results, val):
    if val == 1:
        hist = VHist(results)
        hist.findBreaks(results.t)
        if results.v > 1:
            hist.showBreaks()
        if results.s != 0:
            seg = Segmenter(hist)
            seg.segmentNew()
        return 0, 0
    elif val == 2:
        hist = HHist(results)
        hist.showHist()
        hist.generateHeight(10)
        return 0, 0
    elif val == 3:
        top = TopTrace(results)
        top.lengthFormula()
        if results.g != 0:
            top.removeGaps()
        if results.v > 2:
            top.showTopTrace()
        if results.v > 1:
            top.showBreaks()
        if results.s != 0:
            seg = Segmenter(top)
            seg.segmentNew()
        return 0, 0
    elif val == 4:
        top = TopTrace(results)
        top.lengthFormula()
        if results.v > 1:
            top.showBreaks()
        if results.g != 0:
            top.removeGaps()
        if results.v > 2:
            top.showTopTrace()
        if results.s != 0:
            seg = Segmenter(top)
            seg.segment()
        return 0, 0
    elif val == 5:
        hist = VHist(results)
        hist.findBreaks(results.t)
        if results.v > 1:
            hist.showBreaks()

        top = TopTrace(results)
        top.lengthFormula()
        if results.g != 0:
            top.removeGaps()
        if results.v > 2:
            top.showTopTrace()
        if results.v > 1:
            top.showBreaks()

        return hist.getNumBreaks(), top.getNumBreaks()
    else:
        return 0, 0


def testingOutput(ideal, filename, vertical, topTrace):
    print
    print"--------------"
    print"TESTING OUTPUT"
    print"--------------"
    print"File:", filename
    print"Expected Points:", ideal
    print"Vertical Points:", vertical
    print"Top Trace Points:", topTrace
    print


def menuItems():
    print("Please Select One of the Following:")
    print("\t1) Vertical Hist")
    print("\t2) Horizontal Hist")
    print("\t3) Trace Top (word list)")
    print("\t4) Trace Top (one word)")
    print("\t5) Testing")
    return str(input("Choice: "))


def checkChoice(userVal):
    if not userVal.isdigit():
        return True
    else:
        val = int(userVal)
        if 0 >= val > 5:
            return True

    return False

main()
