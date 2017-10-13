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
            for j in range(i,len(self.breaks),1):
                distance = self.breaks[j] - self.breaks[i]
                prob[i].append((j,distance))

        pprint.pprint(prob)