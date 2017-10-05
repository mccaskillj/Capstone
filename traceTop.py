from PIL import Image


def findFrontRear(pic):
    pos = []

    for i in range(pic.size[0]):
        found = False
        for j in range(pic.size[1]):
            if pic.getpixel((i, j)) < 150:
                found = (i, j)
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


def traceTop(filename):
    pic = Image.open(filename)

    topline = []

    front, rear = findFrontRear(pic)
    topline.append(front)

    pos = 0

    while abs(front[0] - rear[0]) + abs(front[1] - rear[1]) > 10:
        front, pos = nextPixel(pic, pos, front, topline)


def nextPixel(pic, start, curPos, topline):
    offsets = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    positions = []
    for i in range(8):
        positions.append((offsets[i][0] + curPos[0], offsets[i][1] + curPos[1]))

    vals = findNextPixel(pic, start, positions)

    topline.append(offsets[(vals[1] + 4) % 8])

    return vals


def findNextPixel(pic, start, positions):
    for i in range(1, 9):
        if pic.getpixel(positions[(start+i) % 8]) < 100:
            return positions[(start+i) % 8], (start + i + 4) % 8

    exit(0)
    return False

