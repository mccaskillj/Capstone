from PIL import Image

def findFrontRear():
    pic = Image.open("Images/hello.png")

    pos = []

    for i in range(pic.size[0]):
        found = False
        for j in range(pic.size[1]):
            if pic.getpixel((i,j)) < 100:
                found = True
                break
        pos.append(found)

    front = 0
    for i in range(len(pos)):
        if pos[i]:
            front = i
            break

    rear = pic.size[0]
    for i in range(len(pos)-1,-1,-1):
        if pos[i]:
            rear = i
            break

    return front, rear
