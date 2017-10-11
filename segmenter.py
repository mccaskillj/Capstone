from PIL import Image
from pytesseract import image_to_string

class Segmenter:
    filename = ""
    breaks = []
    first = 0
    last = 0

    def __init__(self, hist):
        self.filename = hist.getFilename()
        self.breaks = hist.getBreaks()
        self.first = hist.getFirst()
        self.last = hist.getLast()

    def segment(self):
        print("Segmenting...")
        pic = Image.open(self.filename)
        word = ""
        for i in range(len(self.breaks)-1):
            seg = pic.crop((self.breaks[i],0,self.breaks[i+1],pic.size[1]))
            word += image_to_string(seg, lang="eng2", config="-psm 10")
        print("Segmenting...Completed")
        return word