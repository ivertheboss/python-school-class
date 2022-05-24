import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("3D python test")
icon = pygame.image.load('cube.png')
pygame.display.set_icon(icon)


class Vector3:
    def __init__(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1


class gameObject:
    def __init__(self):
        self.pos = Vector3(0, 0, 0)

    def circle(self,colour):
        pygame.draw.circle(screen, colour, (self.pos.x, self.pos.y), self.pos.z / 50)


class cube:
    def __init__(self):
        self.colour = (255,255,255)
        self.xScale = 1
        self.yScale = 1
        self.zScale = 1
        self.xPos = 0
        self.yPos = 0
        self.zPos = 0
        self.xTemp = "temp"
        self.yTemp = "temp"
        self.zTemp = "temp"
        self.vert1 = gameObject()
        self.vert2 = gameObject()
        self.vert3 = gameObject()
        self.vert4 = gameObject()
        self.vert5 = gameObject()
        self.vert6 = gameObject()
        self.vert7 = gameObject()
        self.vert8 = gameObject()

    def setPositions(self):
        if self.zPos < -340:
            self.zPos = -340
        if not self.zTemp == self.zPos or not self.xTemp == self.xPos or not self.yTemp == self.yPos:
            self.vert4.pos.z = (400 + self.zPos + self.zScale * 50)
            self.vert3.pos.z = (400 + self.zPos + self.zScale * -50)
            self.vert2.pos.z = (400 + self.zPos + self.zScale * 50)
            self.vert1.pos.z = (400 + self.zPos + self.zScale * -50)
            self.vert8.pos.z = (400 + self.zPos + self.zScale * 50)
            self.vert7.pos.z = (400 + self.zPos + self.zScale * -50)
            self.vert6.pos.z = (400 + self.zPos + self.zScale * 50)
            self.vert5.pos.z = (400 + self.zPos + self.zScale * -50)

            self.vert4.pos.x = (400 + self.xPos * (self.vert4.pos.z / 200) + self.xScale * 50 * (self.vert4.pos.z / 200))
            self.vert3.pos.x = (400 + self.xPos * (self.vert3.pos.z / 200) + self.xScale * 50 * (self.vert3.pos.z / 200))
            self.vert2.pos.x = (400 + self.xPos * (self.vert2.pos.z / 200) + self.xScale * 50 * (self.vert2.pos.z / 200))
            self.vert1.pos.x = (400 + self.xPos * (self.vert1.pos.z / 200) + self.xScale * 50 * (self.vert1.pos.z / 200))
            self.vert8.pos.x = (400 + self.xPos * (self.vert8.pos.z / 200) + self.xScale * -50 * (self.vert8.pos.z / 200))
            self.vert7.pos.x = (400 + self.xPos * (self.vert7.pos.z / 200) + self.xScale * -50 * (self.vert7.pos.z / 200))
            self.vert6.pos.x = (400 + self.xPos * (self.vert6.pos.z / 200) + self.xScale * -50 * (self.vert6.pos.z / 200))
            self.vert5.pos.x = (400 + self.xPos * (self.vert5.pos.z / 200) + self.xScale * -50 * (self.vert5.pos.z / 200))

            self.vert4.pos.y = (400 + self.yPos * (self.vert4.pos.z / 200) + self.yScale * -50 * (self.vert4.pos.z / 200))
            self.vert3.pos.y = (400 + self.yPos * (self.vert3.pos.z / 200) + self.yScale * -50 * (self.vert3.pos.z / 200))
            self.vert2.pos.y = (400 + self.yPos * (self.vert2.pos.z / 200) + self.yScale * 50 * (self.vert2.pos.z / 200))
            self.vert1.pos.y = (400 + self.yPos * (self.vert1.pos.z / 200) + self.yScale * 50 * (self.vert1.pos.z / 200))
            self.vert8.pos.y = (400 + self.yPos * (self.vert8.pos.z / 200) + self.yScale * -50 * (self.vert8.pos.z / 200))
            self.vert7.pos.y = (400 + self.yPos * (self.vert7.pos.z / 200) + self.yScale * -50 * (self.vert7.pos.z / 200))
            self.vert6.pos.y = (400 + self.yPos * (self.vert6.pos.z / 200) + self.yScale * 50 * (self.vert6.pos.z / 200))
            self.vert5.pos.y = (400 + self.yPos * (self.vert5.pos.z / 200) + self.yScale * 50 * (self.vert5.pos.z / 200))
        self.xTemp = self.xPos
        self.yTemp = self.yPos
        self.zTemp = self.zPos

    def drawLines(self):
        pygame.draw.line(screen, self.colour, (self.vert8.pos.x, self.vert8.pos.y), (self.vert7.pos.x, self.vert7.pos.y))
        pygame.draw.line(screen, self.colour, (self.vert8.pos.x, self.vert8.pos.y), (self.vert4.pos.x, self.vert4.pos.y))
        pygame.draw.line(screen, self.colour, (self.vert8.pos.x, self.vert8.pos.y), (self.vert6.pos.x, self.vert6.pos.y))

        pygame.draw.line(screen, self.colour, (self.vert2.pos.x, self.vert2.pos.y), (self.vert1.pos.x, self.vert1.pos.y))
        pygame.draw.line(screen, self.colour, (self.vert2.pos.x, self.vert2.pos.y), (self.vert4.pos.x, self.vert4.pos.y))
        pygame.draw.line(screen, self.colour, (self.vert2.pos.x, self.vert2.pos.y), (self.vert6.pos.x, self.vert6.pos.y))

        pygame.draw.line(screen, self.colour, (self.vert5.pos.x, self.vert5.pos.y), (self.vert6.pos.x, self.vert6.pos.y))
        pygame.draw.line(screen, self.colour, (self.vert5.pos.x, self.vert5.pos.y), (self.vert7.pos.x, self.vert7.pos.y))
        pygame.draw.line(screen, self.colour, (self.vert5.pos.x, self.vert5.pos.y), (self.vert1.pos.x, self.vert1.pos.y))

        pygame.draw.line(screen, self.colour, (self.vert3.pos.x, self.vert3.pos.y), (self.vert7.pos.x, self.vert7.pos.y))
        pygame.draw.line(screen, self.colour, (self.vert3.pos.x, self.vert3.pos.y), (self.vert1.pos.x, self.vert1.pos.y))
        pygame.draw.line(screen, self.colour, (self.vert3.pos.x, self.vert3.pos.y), (self.vert4.pos.x, self.vert4.pos.y))

    def generateVertices(self):
        self.vert1.circle((255,255,255))
        self.vert2.circle((255,255,255))
        self.vert3.circle((255,255,255))
        self.vert4.circle((255,255,255))
        self.vert5.circle((255,255,255))
        self.vert6.circle((255,255,255))
        self.vert7.circle((255,255,255))
        self.vert8.circle((255,255,255))

    def initialize(self, DVRT):
        self.setPositions()
        self.drawLines()
        if DVRT:
            self.generateVertices()


myCube = cube()
myCube2 = cube()
myCube3 = cube()
myCube4 = cube()
myCube5 = cube()
myCube2.xPos = 100
myCube3.xPos = -100
myCube4.xPos = 200
myCube5.xPos = -200
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            breakpoint(0)
    screen.fill((0, 0, 0))

    myCube.initialize(True)
    myCube2.initialize(True)
    myCube3.initialize(True)
    myCube4.initialize(True)
    myCube5.initialize(True)

    pygame.display.update()
