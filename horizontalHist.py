from PIL import Image


class HHist:
    hist = []
    first = 0
    last = 0
    max = 0

    def __init__(self, filename):
        pic = Image.open(filename)

        for i in range(pic.size[1]):
            count = 0
            for j in range(pic.size[0]):
                if pic.getpixel((j, i)) < 100:
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

    def append(self, val):
        self.hist.append(val)

    def __repr__(self):
        return str(self.first) + " " + str(self.last) +\
               " " + str(self.max)+ " " + str(self.hist)
