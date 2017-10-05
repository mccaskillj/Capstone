from PIL import Image


def traceTop(filename):
    pic = Image.open(filename)

    print(findFrontRear(pic))


def findFrontRear(pic):
    pos = []

    for i in range(pic.size[0]):
        found = False
        for j in range(pic.size[1]):
            if pic.getpixel((i, j)) < 100:
                found = (i,j)
                break
        pos.append(found)

    front = (0, 0)
    for i in range(len(pos)):
        if pos[i]:
            front = pos[i]
            break

    rear = (0, 0)
    for i in range(len(pos)-1, -1, -1):
        if pos[i]:
            rear = pos[i]
            break

    return front, rear
