from PIL import Image

class HHist:
    hist = []
    first = 0
    last = 0
    max = 0
    height = 0
    filename = ""
    verbose = 0

    def __init__(self, results):
        pic = Image.open(results.filename)
        self.filename = results.filename
        self.verbose = results.v

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

        for i in range(len(self.hist)-1,-1,-1):
            if self.hist[i] > 0:
                self.last = i
                break

        if self.verbose > 0:
            print("Generating horizontal histogram...Complete")

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

    def showHist(self):
        pic = Image.open(self.filename)
        pic.show()
        pic2 = Image.new(pic.mode, pic.size, "white")

        for i in range(len(self.hist)):
            for j in range(self.hist[i]):
                pic2.putpixel((j,i),0)

        pic2.show()


    def generateHeight(self, parts):
        if self.verbose > 0:
            print("Generating base letter height...")
        total = self.last - self.first
        thresh = self.max / parts
        heights = []
        for j in range(parts):
            data = []
            for i in range(self.first-10,self.last+10,1):
                if (self.hist[i]>thresh)!=(self.hist[i+1]>thresh):
                    data.append(i)
            thresh += self.max / parts
            if len(data) > 2:
                new = [0,0]
                for i in range(0,len(data),2):
                    if (data[i+1] - data[i]) > (new[1] - new[0]):
                        new = [data[i],data[i+1]]
                data = new
            if data[1]-data[0] > int(total*0.70):
                data = [0,0]
            elif data[1] - data[0] < int(total*0.30):
                data = [0,0]
            heights.append(data[1] - data[0])
        self.height = max(heights)

        if self.verbose > 0:
            print("Generating base letter height...Complete")

    def getHeight(self):
        return self.height
