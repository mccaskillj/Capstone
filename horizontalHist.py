from PIL import Image


class HHist:

    def __init__(self, results):
        pic = Image.open(results.filename)
        self.filename = results.filename
        self.verbose = results.v
        self.height = 0
        self.bounds = (0, 0)
        self.hist = []
        self.max = 0

        if self.verbose > 0:
            print("Generating horizontal histogram...")

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

        for i in range(len(self.hist)-1, -1, -1):
            if self.hist[i] > 0:
                self.last = i
                break

        if self.verbose > 0:
            print("Generating horizontal histogram...Complete")

    def setFirst(self, first):
        self.first = first

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
               " " + str(self.max) + " " + str(self.hist)

    def showHeight(self):
        pic = Image.open(self.filename)
        for i in range(pic.size[0]):
            pic.putpixel((i, self.bounds[0]),0)
            pic.putpixel((i, self.bounds[1]),0)
        pic.show()

    def showHist(self):
        pic = Image.open(self.filename)
        pic.show()
        pic2 = Image.new(pic.mode, pic.size, "white")

        for i in range(len(self.hist)):
            for j in range(self.hist[i]):
                pic2.putpixel((j, i), 0)

        pic2.show()

    def generateHeight(self, parts):
        if self.verbose > 0:
            print("Generating base letter height...")
        total = self.last - self.first
        thresh = self.max / parts
        heights = []
        TB = []
        for j in range(parts):

            data = []

            for i in range(self.first-10, self.last+10, 1):
                if (self.hist[i] > thresh) != (self.hist[i+1] > thresh):
                    data.append(i)

            thresh += self.max / parts

            if len(data) > 2:
                new = [0, 0]
                for i in range(0, len(data), 2):
                    if (data[i+1] - data[i]) > (new[1] - new[0]):
                        new = [data[i], data[i+1]]
                data = new
            if len(data) == 0:
                continue

            if j < int(parts * 0.3):
                if data[1]-data[0] > int(total*0.70):
                    data = [0, 0]
            if data[1] - data[0] < int(total*0.30):
                data = [0, 0]
            TB.append(data)
            heights.append(data[1] - data[0])

        self.height = max(heights)

        for i in range(len(heights)):
            if heights[i] == self.height:
                self.bounds = TB[i]
                break

        if self.verbose > 0:
            print("Generating base letter height...Complete")

    def generateHeightNew(self,parts):
        return

    def getHeight(self):
        return self.height

    def getBounds(self):
        return self.bounds
