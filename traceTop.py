from PIL import Image
from horizontalHist import *


class TopTrace:
    first = (0, 0)
    last = (0, 0)
    path = []
    height = 0
    bounds = (0,0)
    breaks = []
    filename = ""
    verbose = 0
    low =0
    high = 0
    threshold = 0

    def __init__(self, results):
        pic = Image.open(results.filename)
        self.findFrontRear(pic)
        self.traceTop(pic)

        hist = HHist(results)
        hist.generateHeight(10)
        self.height = hist.getHeight()
        self.bounds = hist.getBounds()
        #hist.showHeight()

        self.filename = results.filename
        self.verbose = results.v
        self.low = results.l
        self.high = results.y
        self.threshold = results.z

    def findFrontRear(self, pic):
        pos = []

        for i in range(pic.size[0]):
            found = False
            for j in range(pic.size[1]):
                if pic.getpixel((i, j)) < 150:
                    found = (i, j)
                    break
            pos.append(found)

        front = (0, 0)
        for i in range(len(pos)):
            if pos[i]:
                front = pos[i]
                break

        rear = (0, 0)
        for i in range(len(pos)-1, -1, -1):
            if pos[i]:
                rear = pos[i]
                break

        self.first = front
        self.last = rear

    def traceTop(self, pic):
        pos = 0

        front = self.first

        while abs(front[0] - self.last[0]) + abs(front[1] - self.last[1]) > 10:
            front, pos = self.nextPixel(pic, pos, front)

    def showTopTrace(self):
        pic = Image.open(self.filename)
        pic2 = Image.new(pic.mode, pic.size,"white")
        point = self.first
        pic2.putpixel(point,0)
        for i in range(len(self.path)):
            point = (point[0]+self.path[i][0], point[1]+self.path[i][1])
            pic2.putpixel(point,0)

        for i in range(pic.size[0]):
            pic2.putpixel((i,self.bounds[0]),0)
            pic2.putpixel((i,self.bounds[1]),0)
        pic2.show()

    def nextPixel(self, pic, start, curPos):
        offsets = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        positions = []
        for i in range(8):
            positions.append((offsets[i][0] + curPos[0], offsets[i][1] + curPos[1]))

        vals = self.findNextPixel(pic, start, positions)

        self.path.append(offsets[(vals[1] + 4) % 8])

        return vals

    def findNextPixel(self, pic, start, positions):
        for i in range(1, 9):
            if pic.getpixel(positions[(start+i) % 8]) < 100:
                return positions[(start+i) % 8], (start + i + 4) % 8

        exit(0)
        return False

    def heightCheck(self):
        front = self.first[0]
        travel = 0
        self.breaks.append(front)
        for i in range(len(self.path)):
            travel += self.path[i][0]
            if travel > int(self.height * 0.5):
                self.breaks.append(front+travel)
                front += travel
                travel = 0
        return

    def checkBounds(self,h):
        if h > self.height:
            return self.height
        if h < 0:
            return 0
        return h

    def travelAlgorithm(self, h):
        return self.low - (h*((self.low - self.high)/self.height))


    def lengthFormula(self):
        height = self.bounds[1] - self.first[1]
        width = self.first[0]
        total = 0.0
        self.breaks.append(width)
        for i in range(len(self.path)):
            height += self.path[i][1] * -1
            width += self.path[i][0]
            val = self.travelAlgorithm(self.checkBounds(height))
            total += val * self.path[i][0]
            if (total > (self.height * self.threshold / 100)):
                self.breaks.append(width)
                total = 0.0
        self.breaks.append(self.last[0])
        return

    def showBreaks(self):
        pic = Image.open(self.filename)
        for i in range(len(self.breaks)):
            for j in range(pic.size[1]):
                pic.putpixel((self.breaks[i], j), 0)
        pic.show()

    def removeGaps(self):
        pic = Image.open(self.filename)
        for i in range(len(self.breaks)-1, -1, -1):
            count = 0
            flips = 0
            for j in range(self.bounds[0]+25,self.bounds[1],1):
                if (pic.getpixel((self.breaks[i],j)) < 100) != (pic.getpixel((self.breaks[i], j+1)) < 100):
                    flips += 1
                if pic.getpixel((self.breaks[i],j)) < 100:
                    count += 1
                pic.putpixel((self.breaks[i],j),0)
            if flips > 3:
                self.breaks.pop(i)

            if count > int((self.bounds[1] - self.bounds[0])*0.4):
                self.breaks.pop(i)

    def getFilename(self):
        return self.filename

    def getBreaks(self):
        return self.breaks

    def getNumBreaks(self):
        return len(self.breaks)

    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last

    def getVerbose(self):
        return self.verbose

    def getHeight(self):
        return self.height