from PIL import Image
from pytesseract import image_to_string
from tesserocr import PyTessBaseAPI, PSM
from operator import itemgetter
import pprint

class Segmenter:
    filename = ""
    breaks = []
    first = 0
    last = 0
    verbose = 0
    height = 0
    words = []

    def __init__(self, method):
        self.filename = method.getFilename()
        self.breaks = method.getBreaks()
        self.first = method.getFirst()
        self.last = method.getLast()
        self.verbose = method.getVerbose()
        self.height = method.getHeight()

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
        print(word)
        return word

    def segmentNew(self):
        if self.verbose > 0:
            print("Segmenting...")

        pic = Image.open(self.filename)

        prob = []
        letter = ""
        conf = 0
        for i in range(len(self.breaks)-1):
            prob.append([])
            for j in range(i, len(self.breaks), 1):
                distance = self.breaks[j] - self.breaks[i]
                if int(self.height * 0.3) < distance < int(self.height * 1.65):
                    with PyTessBaseAPI(psm=10,lang="eng2") as api:
                        seg = pic.crop((self.breaks[i],0,self.breaks[j],pic.size[1]))
                        api.SetImage(seg)
                        letter = api.GetUTF8Text()
                        conf = api.AllWordConfidences()
                        #letter = image_to_string(seg, lang="eng2", config="-psm 10")
                    ratio = float(distance)/float(self.height)
                    prob[i].append((j, conf[0], str(letter[0]).lower()))

        if self.verbose > 0:
            print("Segmenting...Complete")
            print("Building words...")
        self.buildWords(prob, 0, "",0,0)
        pprint.pprint(self.words[0:15])
        #print(self.build(prob))
        if self.verbose > 0:
            print("Building words...Complete")

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

    def build(self,prob):
        pos = 0
        word = ""
        while pos < len(prob) and len(prob[pos]) != 0:
            max=0
            ind = 0
            for i in range(len(prob[pos])):
                if prob[pos][i][1] > max:
                    max = prob[pos][i][1]
                    ind = i
            word += prob[pos][ind][2]
            pos = prob[pos][ind][0]

        return word

    def buildWords(self, prob, index, word, sum, count):
        if index == len(prob):
            self.words.append([word, float(sum)/float(count),len(word)])
            return True
        for i in range(len(prob[index])):
            if prob[index][i][2] is not None:
                word += prob[index][i][2]
                count += 1
                sum += prob[index][i][1]
                self.buildWords(prob, prob[index][i][0], word, sum, count)
                sum -= prob[index][i][1]
                count -= 1
                word = word[:-1]

        self.words.sort(key=itemgetter(1,2),reverse=True)

        return False
