from PIL import Image


def horizontalHist(filename):
    pic1 = Image.open(filename)

    hist = []

    for i in range(pic1.size[1]):
        count = 0
        for j in range(pic1.size[0]):
            if pic1.getpixel((j,i)) < 100:
                count += 1
        hist.append(count)

    pic2 = Image.new(pic1.mode, pic1.size, 255)

    for i in range(len(hist)):
        for j in range(hist[i]):
            pic2.putpixel((j,i),0)

    pic1.show()
    pic2.show()
