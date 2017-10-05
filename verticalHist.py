from PIL import Image

pic1 = Image.open("Images/hello.png")

hist = []

for i in range(pic1.size[0]):
    count = 0
    for j in range(pic1.size[1]):
        col = pic1.getpixel((i, j))
        pic1.putpixel((i,j),col)
        if col < 100:
            count += 1
    hist.append(count)

print(hist)

pic2 = Image.new(pic1.mode,pic1.size)

for i in range(pic2.size[0]):
    for j in range(pic2.size[1]):
        pic2.putpixel((i, j), 255)

for i in range(len(hist)):
    for j in range(int(2.5*hist[i])):
        pic2.putpixel((i, j), 0)

pic1.show()
pic2.show()
