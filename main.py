import pygame
import sys
from constants import *


def initGame():
    global fpsClock, windowDimensions, mainWindow
    pygame.init()
    fpsClock = pygame.time.Clock()
    windowDimensions = (0, 0)
    mainWindow = pygame.display.set_mode(windowDimensions, pygame.FULLSCREEN | pygame.DOUBLEBUF)
    windowDimensions = (mainWindow.get_size())
    pygame.display.set_caption('Stick Wars')
    mainWindow.fill(background_colour)

    global scrollOffsetX, scrollOffsetY
    scrollOffsetX, scrollOffsetY = 0, 0

    # Read map file and set map constants
    file_pointer = open("map1.txt", "r")
    map1 = file_pointer.readlines()
    file_pointer.close()
    global mapWidth, mapHeight, mapBoxSize, mapWidthPix, mapHeightPix
    mapWidth = int(map1[0])
    mapHeight = int(map1[1])
    mapBoxSize = int(map1[2])
    mapWidthPix = mapWidth * mapBoxSize
    mapHeightPix = mapHeight * mapBoxSize

    # Build map array
    global gameMap
    gameMap = []
    # i is an increment to reference the map1 list
    i = 3
    # Iterate through gameMap and fill it with the info from map1
    for row in range(mapHeight):
        gameMap.append([])
        for column in range(mapWidth):
            line = map1[i].split(".")
            i += 1
            for z in range(len(line)):
                line[z] = line[z].rstrip("\n")
            building, unit = None, None
            terrain = line[0]
            if len(line) > 1:
                building = line[1]
            if len(line) == 3:
                unit = line[2]

            gameMap[row].append({
                "terrain" : terrain,
                "building" : building,
                "unit" : unit
                })
    # for a in gameMap:
    #     for b in a:
    #         print b


def checkEvents():
    global scrollOffsetX, scrollOffsetY
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if mainWindow.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode(windowDimensions, pygame.DOUBLEBUF | pygame.RESIZABLE)
                else:
                    pygame.display.set_mode(windowDimensions, pygame.FULLSCREEN | pygame.DOUBLEBUF)
            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif event.key == pygame.K_LEFT:
                scrollController("left")
            elif event.key == pygame.K_RIGHT:
                scrollController("right")
            elif event.key == pygame.K_UP:
                scrollController("up")
            elif event.key == pygame.K_DOWN:
                scrollController("down")
        # Fullscreen Toggle
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_LEFT]:
        scrollController("left")
    elif keys[pygame.K_RIGHT]:
        scrollController("right")
    elif keys[pygame.K_UP]:
        scrollController("up")
    elif keys[pygame.K_DOWN]:
        scrollController("down")


def scrollController(direction):
    global minScrollX, maxScrollX, minScrollY, maxScrollY
    global scrollOffsetX, scrollOffsetY
    def valueClamp(value, minValue, maxValue):
        return max(min(value, maxValue), minValue)
    if direction == "left":
        scrollOffsetX -= scrollFactor
        scrollOffsetX = valueClamp(scrollOffsetX, minScrollX, maxScrollX)
    elif direction == "right":
        scrollOffsetX += scrollFactor
        scrollOffsetX = valueClamp(scrollOffsetX, minScrollX, maxScrollX)
    elif direction == "up":
        scrollOffsetY -= scrollFactor
        scrollOffsetY = valueClamp(scrollOffsetY, minScrollY, maxScrollY)
    else:
        scrollOffsetY += scrollFactor
        scrollOffsetY = valueClamp(scrollOffsetY, minScrollY, maxScrollY)





def beginningLoopStuff():
    pygame.transform.flip(mainWindow, True, True)


def calculateScrolling():
    global mapWidthPix, mapHeightPix
    # Calculate Scrolling Min and Max
    global minScrollX, maxScrollX, minScrollY, maxScrollY
    (x, y) = mainWindow.get_size()
    minScrollX, minScrollY = 0, 0
    if x >= mapWidthPix:
        maxScrollX = 0
    else:
        maxScrollX = mapWidthPix - x
    if y >= mapHeightPix:
        maxScrollY = 0
    else:
        maxScrollY = mapHeightPix - y



def endLoopStuff():
    pygame.transform.flip(mainWindow, True, True)
    pygame.display.update()
    fpsClock.tick(120)


def draw():
    mainWindow.fill(colors['lightGreen'])
    # Draw grid
    global mapWidth, mapHeight, mapBoxSize
    global scrollOffsetX, scrollOffsetY
    # Draw outside border
    xmin = -scrollOffsetX
    ymin = -scrollOffsetY
    xmax = (mapWidth * mapBoxSize) - scrollOffsetX
    ymax = (mapHeight * mapBoxSize) - scrollOffsetY
    corner1 = (xmin, ymin)
    corner2 = (xmax, ymin)
    corner3 = (xmin, ymax)
    corner4 = (xmax, ymax)
    pygame.draw.line(mainWindow, colors['black'], corner1, corner2, gridWidth)
    # pygame.draw.line(mainWindow, colors['black'], corner2, corner4, gridWidth)
    # pygame.draw.line(mainWindow, colors['black'], corner4, corner3, gridWidth)
    pygame.draw.line(mainWindow, colors['black'], corner3, corner1, gridWidth)

    # Draw Grid
    for i in range(mapWidth):
        x = (mapBoxSize * i + mapBoxSize) - scrollOffsetX
        pygame.draw.line(mainWindow, colors['black'], (x, ymin), (x, ymax))
    for i in range(mapHeight):
        y = (mapBoxSize * i + mapBoxSize) - scrollOffsetY
        pygame.draw.line(mainWindow, colors['black'], (xmin, y), (xmax, y))
    # pygame.draw.circle(mainWindow, colors['black'], (300 + scrollOffsetX, 300 + scrollOffsetY), 100)
    # Test image drawing
    image = pygame.image.load("graphics/infantry.png")
    image = pygame.transform.scale(image, (mapBoxSize, mapBoxSize))
    mainWindow.blit(image, (xmin, ymin))






initGame()
while True:
    beginningLoopStuff()
    calculateScrolling()
    draw()
    checkEvents()
    endLoopStuff()