from PIL import Image
from pytesseract import image_to_string
import pprint

class Segmenter:
    filename = ""
    breaks = []
    first = 0
    last = 0
    verbose = 0
    height = 0
    words = []

    def __init__(self, hist):
        self.filename = hist.getFilename()
        self.breaks = hist.getBreaks()
        self.first = hist.getFirst()
        self.last = hist.getLast()
        self.verbose = hist.getVerbose()
        self.height = hist.getHeight()

    def segment(self):
        if self.verbose > 0:
            print("Segmenting...")
        pic = Image.open(self.filename)
        word = ""
        for i in range(len(self.breaks)-1):
            seg = pic.crop((self.breaks[i],0,self.breaks[i+1],pic.size[1]))
            letter = image_to_string(seg, lang="eng2", config="-psm 10")
            word += letter

        if self.verbose > 0:
            print("Segmenting...Completed")
        return word

    def segmentNew(self):
        if self.verbose > 0:
            print("Segmenting...")

        pic = Image.open(self.filename)

        prob = []
        for i in range(len(self.breaks)-1):
            prob.append([])
            for j in range(i, len(self.breaks), 1):
                distance = self.breaks[j] - self.breaks[i]
                if int(self.height * 0.3) < distance < int(self.height * 1.65):
                    seg = pic.crop((self.breaks[i],0,self.breaks[j],pic.size[1]))
                    letter = image_to_string(seg, lang="eng2", config="-psm 10")
                    ratio = float(distance)/float(self.height)
                    if self.letterSizeCheck(ratio,str(letter)):
                        prob[i].append((j, ratio, str(letter)))
                    else:
                        prob[i].append((j,ratio,None))
                else:
                    prob[i].append((j, None, None))

        pprint.pprint(prob)
        if self.verbose > 0:
            print("Segmenting...Complete")
            print("Building words...")
        self.buildWords(prob, 0, "")
        if self.verbose > 0:
            print("Building words...Complete")
        print(self.words)

    def letterSizeCheck(self, size, val):
        if val.lower() == 'i':
            if 0.8 < size or size < 0.55:
                return False
        elif val.lower() == 'e':
            if 0.8 < size or size < 0.60:
                return False
        elif val.lower() == 'm':
            if 1.6 < size or size < 1.35:
                return False
        elif val.lower() == 'w':
            if 1.6 < size or size < 1.35:
                return False
        return True

    def buildWords(self, prob, index, word):
        if index == len(prob):
            self.words.append(word)
            return True
        for i in range(len(prob[index])):
            if prob[index][i][2] is not None:
                word += prob[index][i][2]
                self.buildWords(prob, prob[index][i][0], word)
                word = word[:-1]

        return False
