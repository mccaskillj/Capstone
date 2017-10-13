from PIL import Image


class TopTrace:
    first = (0, 0)
    last = (0, 0)
    path = []

    def __init__(self, results):
        pic = Image.open(results.filename)
        self.findFrontRear(pic)
        self.traceTop(pic)

    def findFrontRear(self, pic):
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

        self.first = front
        self.last = rear

    def traceTop(self, pic):
        pos = 0

        front = self.first

        while abs(front[0] - self.last[0]) + abs(front[1] - self.last[1]) > 10:
            front, pos = self.nextPixel(pic, pos, front)

    def nextPixel(self, pic, start, curPos):
        offsets = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        positions = []
        for i in range(8):
            positions.append((offsets[i][0] + curPos[0], offsets[i][1] + curPos[1]))

        vals = self.findNextPixel(pic, start, positions)

        self.path.append(offsets[(vals[1] + 4) % 8])

        return vals

    def findNextPixel(self, pic, start, positions):
        for i in range(1, 9):
            if pic.getpixel(positions[(start+i) % 8]) < 100:
                return positions[(start+i) % 8], (start + i + 4) % 8

        exit(0)
        return False

