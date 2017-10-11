from PIL import Image


class VHist:
    hist = []
    first = 0
    last = 0
    max = 0
    breaks = []
    filename = ""

    def __init__(self, filename):
        pic = Image.open(filename)
        self.filename = filename

        for i in range(pic.size[0]):
            count = 0
            for j in range(pic.size[1]):
                if pic.getpixel((i, j)) < 100:
                    count += 1
            self.hist.append(count)
            if count > self.max:
                self.max = count

        for i in range(len(self.hist)):
            if self.hist[i] > 0:
                self.first = i
                break

        for i in range(len(self.hist)-1,-1,-1):
            if self.hist[i] > 0:
                self.last = i
                break

    def setFirst(self, first):
        self.first =first

    def getFirst(self):
        return self.first

    def setLast(self, last):
        self.last = last

    def getLast(self):
        return self.last

    def getFilename(self):
        return self.filename

    def getBreaks(self):
        return self.breaks

    def append(self, val):
        self.hist.append(val)

    def __repr__(self):
        return str(self.first) + " " + str(self.last) +\
               " " + str(self.max)+ " " + str(self.hist)

    def findBreaks(self, percent):
        thresh = self.max * percent // 100
        pivots = []
        for i in range(len(self.hist)-2):
            if (self.hist[i] > thresh) != (self.hist[i+1] > thresh):
                pivots.append(i)

        self.breaks.append((pivots[0]+self.first)//2)

        for i in range(1,len(pivots)-2,2):
            self.breaks.append((pivots[i]+pivots[i+1])//2)

        self.breaks.append((pivots[-1] + self.last) // 2)

    def showBreaks(self):
        pic = Image.open(self.filename)
        for i in range(len(self.breaks)):
            for j in range(pic.size[1]):
                pic.putpixel((self.breaks[i],j), 0)
        pic.show()



