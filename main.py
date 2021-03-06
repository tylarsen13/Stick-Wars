import pygame
import sys
from constants import *
import math

from units import Infantry, Tank, Artillery, Fighter, Missiles, AquaticTransport


def initGame():
    global fpsClock, windowDimensions, mainWindow
    pygame.init()
    fpsClock = pygame.time.Clock()
    windowDimensions = (0, 0)
    mainWindow = pygame.display.set_mode(windowDimensions, pygame.FULLSCREEN | pygame.DOUBLEBUF)
    windowDimensions = (mainWindow.get_size())
    pygame.display.set_caption('Stick Wars')

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
            if len(line) > 2:
                command = "unit = " + line[2] + "(" + line[3] + ", " + line[4] + ")"
                exec command
                # Normalize initial unit HP
                unit.hp = math.ceil(unit.hp*10)/10
            gameMap[row].append({
                "terrain" : terrain,
                "building" : building,
                "unit" : unit
                })

    loadImages()
    # Initalize Fonts
    pygame.font.init()
    global gameFont
    gameFont = pygame.font.Font(None, mapBoxSize / 4)

    global optionFont
    optionFont = pygame.font.Font(None, 45)

    # Set selected unit to none
    global selectedUnit
    selectedUnit = None
    global selectedUnitMap
    selectedUnitMap = None

    # Set highlighted square to empty list
    global highlightedSquares
    highlightedSquares = [] 
    global checkedSquares 
    checkedSquares = []
    global drawOptions
    drawOptions = None
    global selectedUnitOptions
    selectedUnitOptions = []
    global menuOn
    menuOn = False
    global menuCorner
    menuCorner = None
    global selectedUnitAttacks
    selectedUnitAttacks = []
    global attackOn
    attackOn = False
    global turn
    turn = 1

    # for a in gameMap:
    #     for b in a:
    #         print b


def loadImages():
    global infantryImage1, infantryImage2, infantryImage3, infantryImage4
    infantryImage1 = pygame.image.load("graphics/infantry1.png").convert_alpha()
    infantryImage2 = pygame.image.load("graphics/infantry2.png").convert_alpha()
    infantryImage3 = pygame.image.load("graphics/infantry3.png").convert_alpha()
    infantryImage4 = pygame.image.load("graphics/infantry4.png").convert_alpha()
    infantryImage1 = pygame.transform.scale(infantryImage1, (mapBoxSize, mapBoxSize))
    infantryImage2 = pygame.transform.scale(infantryImage2, (mapBoxSize, mapBoxSize))
    infantryImage3 = pygame.transform.scale(infantryImage3, (mapBoxSize, mapBoxSize))
    infantryImage4 = pygame.transform.scale(infantryImage4, (mapBoxSize, mapBoxSize))

    global infantryImage1inactive, infantryImage2inactive, infantryImage3inactive, infantryImage4inactive
    infantryImage1inactive = pygame.image.load("graphics/infantry1inactive.png").convert_alpha()
    infantryImage2inactive = pygame.image.load("graphics/infantry2inactive.png").convert_alpha()
    infantryImage3inactive = pygame.image.load("graphics/infantry3inactive.png").convert_alpha()
    infantryImage4inactive = pygame.image.load("graphics/infantry4inactive.png").convert_alpha()
    infantryImage1inactive = pygame.transform.scale(infantryImage1inactive, (mapBoxSize, mapBoxSize))
    infantryImage2inactive = pygame.transform.scale(infantryImage2inactive, (mapBoxSize, mapBoxSize))
    infantryImage3inactive = pygame.transform.scale(infantryImage3inactive, (mapBoxSize, mapBoxSize))
    infantryImage4inactive = pygame.transform.scale(infantryImage4inactive, (mapBoxSize, mapBoxSize))


    global tankImage1, tankImage2, tankImage3, tankImage4
    tankImage1 = pygame.image.load("graphics/tank1.png").convert_alpha()
    tankImage2 = pygame.image.load("graphics/tank2.png").convert_alpha()
    tankImage3 = pygame.image.load("graphics/tank3.png").convert_alpha()
    tankImage4 = pygame.image.load("graphics/tank4.png").convert_alpha()
    tankImage1 = pygame.transform.scale(tankImage1, (mapBoxSize, mapBoxSize))
    tankImage2 = pygame.transform.scale(tankImage2, (mapBoxSize, mapBoxSize))
    tankImage3 = pygame.transform.scale(tankImage3, (mapBoxSize, mapBoxSize))
    tankImage4 = pygame.transform.scale(tankImage4, (mapBoxSize, mapBoxSize))

    global tankImage1inactive, tankImage2inactive, tankImage3inactive, tankImage4inactive
    tankImage1inactive = pygame.image.load("graphics/tank1inactive.png").convert_alpha()
    tankImage2inactive = pygame.image.load("graphics/tank2inactive.png").convert_alpha()
    tankImage3inactive = pygame.image.load("graphics/tank3inactive.png").convert_alpha()
    tankImage4inactive = pygame.image.load("graphics/tank4inactive.png").convert_alpha()
    tankImage1inactive = pygame.transform.scale(tankImage1inactive, (mapBoxSize, mapBoxSize))
    tankImage2inactive = pygame.transform.scale(tankImage2inactive, (mapBoxSize, mapBoxSize))
    tankImage3inactive = pygame.transform.scale(tankImage3inactive, (mapBoxSize, mapBoxSize))
    tankImage4inactive = pygame.transform.scale(tankImage4inactive, (mapBoxSize, mapBoxSize))


    global artilleryImage1, artilleryImage2, artilleryImage3, artilleryImage4
    artilleryImage1 = pygame.image.load("graphics/artillery1.png").convert_alpha()
    artilleryImage2 = pygame.image.load("graphics/artillery2.png").convert_alpha()
    artilleryImage3 = pygame.image.load("graphics/artillery3.png").convert_alpha()
    artilleryImage4 = pygame.image.load("graphics/artillery4.png").convert_alpha()
    artilleryImage1 = pygame.transform.scale(artilleryImage1, (mapBoxSize, mapBoxSize))
    artilleryImage2 = pygame.transform.scale(artilleryImage2, (mapBoxSize, mapBoxSize))
    artilleryImage3 = pygame.transform.scale(artilleryImage3, (mapBoxSize, mapBoxSize))
    artilleryImage4 = pygame.transform.scale(artilleryImage4, (mapBoxSize, mapBoxSize))

    global artilleryImage1inactive, artilleryImage2inactive, artilleryImage3inactive, artilleryImage4inactive
    artilleryImage1inactive = pygame.image.load("graphics/artillery1inactive.png").convert_alpha()
    artilleryImage2inactive = pygame.image.load("graphics/artillery2inactive.png").convert_alpha()
    artilleryImage3inactive = pygame.image.load("graphics/artillery3inactive.png").convert_alpha()
    artilleryImage4inactive = pygame.image.load("graphics/artillery4inactive.png").convert_alpha()
    artilleryImage1inactive = pygame.transform.scale(artilleryImage1inactive, (mapBoxSize, mapBoxSize))
    artilleryImage2inactive = pygame.transform.scale(artilleryImage2inactive, (mapBoxSize, mapBoxSize))
    artilleryImage3inactive = pygame.transform.scale(artilleryImage3inactive, (mapBoxSize, mapBoxSize))
    artilleryImage4inactive = pygame.transform.scale(artilleryImage4inactive, (mapBoxSize, mapBoxSize))

    global fighterImage1, fighterImage2, fighterImage3, fighterImage4
    fighterImage1 = pygame.image.load("graphics/fighter1.png").convert_alpha()
    fighterImage2 = pygame.image.load("graphics/fighter2.png").convert_alpha()
    fighterImage3 = pygame.image.load("graphics/fighter3.png").convert_alpha()
    fighterImage4 = pygame.image.load("graphics/fighter4.png").convert_alpha()
    fighterImage1 = pygame.transform.scale(fighterImage1, (mapBoxSize, mapBoxSize))
    fighterImage2 = pygame.transform.scale(fighterImage2, (mapBoxSize, mapBoxSize))
    fighterImage3 = pygame.transform.scale(fighterImage3, (mapBoxSize, mapBoxSize))
    fighterImage4 = pygame.transform.scale(fighterImage4, (mapBoxSize, mapBoxSize))

    global fighterImage1inactive, fighterImage2inactive, fighterImage3inactive, fighterImage4inactive
    fighterImage1inactive = pygame.image.load("graphics/fighter1inactive.png").convert_alpha()
    fighterImage2inactive = pygame.image.load("graphics/fighter2inactive.png").convert_alpha()
    fighterImage3inactive = pygame.image.load("graphics/fighter3inactive.png").convert_alpha()
    fighterImage4inactive = pygame.image.load("graphics/fighter4inactive.png").convert_alpha()
    fighterImage1inactive = pygame.transform.scale(fighterImage1inactive, (mapBoxSize, mapBoxSize))
    fighterImage2inactive = pygame.transform.scale(fighterImage2inactive, (mapBoxSize, mapBoxSize))
    fighterImage3inactive = pygame.transform.scale(fighterImage3inactive, (mapBoxSize, mapBoxSize))
    fighterImage4inactive = pygame.transform.scale(fighterImage4inactive, (mapBoxSize, mapBoxSize))

    global aquatictransportImage1, aquatictransportImage2, aquatictransportImage3, aquatictransportImage4
    aquatictransportImage1 = pygame.image.load("graphics/aquatictransport1.png").convert_alpha()
    aquatictransportImage2 = pygame.image.load("graphics/aquatictransport2.png").convert_alpha()
    aquatictransportImage3 = pygame.image.load("graphics/aquatictransport3.png").convert_alpha()
    aquatictransportImage4 = pygame.image.load("graphics/aquatictransport4.png").convert_alpha()
    aquatictransportImage1 = pygame.transform.scale(aquatictransportImage1, (mapBoxSize, mapBoxSize))
    aquatictransportImage2 = pygame.transform.scale(aquatictransportImage2, (mapBoxSize, mapBoxSize))
    aquatictransportImage3 = pygame.transform.scale(aquatictransportImage3, (mapBoxSize, mapBoxSize))
    aquatictransportImage4 = pygame.transform.scale(aquatictransportImage4, (mapBoxSize, mapBoxSize))

    global aquatictransportImage1inactive, aquatictransportImage2inactive, aquatictransportImage3inactive, aquatictransportImage4inactive
    aquatictransportImage1inactive = pygame.image.load("graphics/aquatictransport1inactive.png").convert_alpha()
    aquatictransportImage2inactive = pygame.image.load("graphics/aquatictransport2inactive.png").convert_alpha()
    aquatictransportImage3inactive = pygame.image.load("graphics/aquatictransport3inactive.png").convert_alpha()
    aquatictransportImage4inactive = pygame.image.load("graphics/aquatictransport4inactive.png").convert_alpha()
    aquatictransportImage1inactive = pygame.transform.scale(aquatictransportImage1inactive, (mapBoxSize, mapBoxSize))
    aquatictransportImage2inactive = pygame.transform.scale(aquatictransportImage2inactive, (mapBoxSize, mapBoxSize))
    aquatictransportImage3inactive = pygame.transform.scale(aquatictransportImage3inactive, (mapBoxSize, mapBoxSize))
    aquatictransportImage4inactive = pygame.transform.scale(aquatictransportImage4inactive, (mapBoxSize, mapBoxSize))


def checkEvents():
    global scrollOffsetX, scrollOffsetY, windowDimensions, turn
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
            elif event.key == pygame.K_e:
                # End turn
                reactivateUnits()
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
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
            mousePos = event.pos
            button = event.button
            mouseWasClicked(mousePos, button)

        elif event.type == pygame.VIDEORESIZE:
            windowDimensions = event.dict['size']

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
    (x, y) = windowDimensions
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
    # pygame.transform.flip(mainWindow, True, True)
    pygame.display.update()
    fpsClock.tick(30)


def calculateMoveDistance(x1, y1, x2, y2):
    difx = abs(x1 - x2)
    dify = abs(y1 - y2)
    return difx + dify


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
        pygame.draw.line(mainWindow, colors['black'], (x, ymin), (x, ymax), gridWidth)
    for i in range(mapHeight):
        y = (mapBoxSize * i + mapBoxSize) - scrollOffsetY
        pygame.draw.line(mainWindow, colors['black'], (xmin, y), (xmax, y), gridWidth)
    # pygame.draw.circle(mainWindow, colors['black'], (300 + scrollOffsetX, 300 + scrollOffsetY), 100)
    
    # Draw Terrain
    global gameMap, gameFont
    global infantryImage1, infantryImage2, infantryImage3, infantryImage4
    global infantryImage1inactive, infantryImage2inactive, infantryImage3inactive, infantryImage4inactive
    global tankImage1, tankImage2, tankImage3, tankImage4
    global tankImage1inactive, tankImage2inactive, tankImage3inactive, tankImage4inactive
    global artilleryImage1, artilleryImage2, artilleryImage3, artilleryImage4
    global artilleryImage1inactive, artilleryImage2inactive, artilleryImage3inactive, artilleryImage4inactive
    global fighterImage1, fighterImage2, fighterImage3, fighterImage4
    global fighterImage1inactive, fighterImage2inactive, fighterImage3inactive, fighterImage4inactive
    global aquatictransportImage1, aquatictransportImage2, aquatictransportImage3, aquatictransportImage4
    global aquatictransportImage1inactive, aquatictransportImage2inactive, aquatictransportImage3inactive, aquatictransportImage4inactive
    for i in range(mapHeight):
        for j in range(mapWidth):
            t = gameMap[i][j]["terrain"]
            if t == "plain":
                color = colors['lightGreen']
            elif t == "sea":
                color = colors['blue']
            rectangle = pygame.Rect(0, 0, 0, 0)
            x = (mapBoxSize * j + mapBoxSize) - scrollOffsetX
            y = (mapBoxSize * i + mapBoxSize) - scrollOffsetY
            x -= (mapBoxSize / 2)
            y -= (mapBoxSize / 2)
            rectangle.width = mapBoxSize - gridWidth
            rectangle.height = mapBoxSize - gridWidth
            rectangle.center = (x, y)
            pygame.draw.rect(mainWindow, color, rectangle)
            # Draw Units
            u = gameMap[i][j]["unit"]
            if u != None:
                unit = u.unitType.lower()
                command = "image = " + unit + "Image" + str(u.team)
                if not u.active:
                    command += "inactive"
                exec command
                x -= (mapBoxSize / 2)
                y -= (mapBoxSize / 2)
                mainWindow.blit(image, (x, y))
                # Draw Hit Points
                mainWindow.blit((gameFont.render(str(u.hp), False, colors['white'], colors['black'])), (x, y))

    # Draw available movements for selected unit
    global highlightedSquares
    for square in highlightedSquares:
        y, x = square
        s = pygame.Surface((mapBoxSize, mapBoxSize), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((0, 0, 255, 128))                         # notice the alpha value in the color
        mainWindow.blit(s, (x * mapBoxSize - scrollOffsetX, y * mapBoxSize - scrollOffsetY))

    # Draw options after moving unit
    global drawOptions, optionFont
    if drawOptions != None:
        rect1dim = drawOptions[0]
        rect1 = pygame.Rect(0, 0, 0, 0)
        rect1.height = rect1dim[0]
        rect1.width = rect1dim[1]
        rect1.center = rect1dim[2]
        pygame.draw.rect(mainWindow, colors['lightYellow'], rect1)
        for i in range(len(drawOptions) - 1):
            string = drawOptions[i + 1][0]
            center = drawOptions[i + 1][1]
            mainWindow.blit((optionFont.render(string, False, colors['white'], colors['black'])), center)

    global attackOn, selectedUnitAttacks
    if attackOn:
        for square in selectedUnitAttacks:
            x, y = square
            s = pygame.Surface((mapBoxSize, mapBoxSize), pygame.SRCALPHA)   # per-pixel alpha
            s.fill((255, 0, 0, 128))                         # notice the alpha value in the color
            mainWindow.blit(s, (x * mapBoxSize - scrollOffsetX, y * mapBoxSize - scrollOffsetY))


def isTerrainValid(x, y):
    global ox, oy, gameMap
    if gameMap[y][x]['terrain'] in gameMap[oy][ox]['unit'].validTerrain:
        return True
    else:
        return False


def checkPrev(x, y, prevX, prevY):
    if x == prevX and y == prevY:
        return False
    else:
        return True


def findAvailableMoves(x, y, moveAbility, prevX, prevY):
    global ox, oy, highlightedSquares, gameMap, checkedSquares
    global mapWidth, mapHeight
    if calculateMoveDistance(ox, oy, x, y) < moveAbility:
        if x + 1 <= mapWidth - 1:
            if not (x + 1, y) in checkedSquares:
                checkedSquares.append((x + 1, y))
                if checkPrev(x + 1, y, prevX, prevY):
                    if gameMap[y][x + 1]['unit'] == None:
                        if isTerrainValid(x + 1, y):
                            highlightedSquares.append((y, x + 1))
                            findAvailableMoves(x + 1, y, moveAbility, x, y)
                    elif gameMap[oy][ox]['unit'].team == gameMap[y][x + 1]['unit'].team:
                        findAvailableMoves(x + 1, y, moveAbility, x, y)
        if x - 1 >= 0:
            if not (x - 1, y) in checkedSquares:
                checkedSquares.append((x - 1, y))
                if checkPrev(x - 1, y, prevX, prevY):
                    if gameMap[y][x - 1]['unit'] == None:
                        if isTerrainValid(x - 1, y):
                            highlightedSquares.append((y, x - 1))
                            findAvailableMoves(x - 1, y, moveAbility, x, y)
                    elif gameMap[oy][ox]['unit'].team == gameMap[y][x - 1]['unit'].team:
                        findAvailableMoves(x - 1, y, moveAbility, x, y)
        if y + 1 <= mapHeight - 1:
            if not (x, y + 1) in checkedSquares:
                checkedSquares.append((x, y + 1))
                if checkPrev(x, y + 1, prevX, prevY):
                    if gameMap[y + 1][x]['unit'] == None:
                        if isTerrainValid(x, y + 1):
                            highlightedSquares.append((y + 1, x))
                            findAvailableMoves(x, y + 1, moveAbility, x, y)
                    elif gameMap[oy][ox]['unit'].team == gameMap[y + 1][x]['unit'].team:
                        findAvailableMoves(x, y + 1, moveAbility, x, y)
        if y - 1 >= 0:
            if not (x, y - 1) in checkedSquares:
                checkedSquares.append((x, y - 1))
                if checkPrev(x, y - 1, prevX, prevY):
                    if gameMap[y - 1][x]['unit'] == None:
                        if isTerrainValid(x, y - 1):
                            highlightedSquares.append((y - 1, x))
                            findAvailableMoves(x, y - 1, moveAbility, x, y)
                    elif gameMap[oy][ox]['unit'].team == gameMap[y - 1][x]['unit'].team:
                        findAvailableMoves(x, y - 1, moveAbility, x, y)


def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]


def generateSelectedUnitRadar():
    # Which squares need to appear selected? We need to tell the draw function
    global highlightedSquares
    highlightedSquares = []

    global ox, oy
    oy, ox = selectedUnit
    unit = gameMap[oy][ox]["unit"]
    findAvailableMoves(ox, oy, unit.moveAbility, ox, oy)
    highlightedSquares.append((oy, ox))
    highlightedSquares = f7(highlightedSquares)


def generateSelectedUnitOptions(x, y):
    global gameMap, mapHeight, mapWidth, selectedUnitOptions, selectedUnitAttacks
    selectedUnitOptions = []
    if gameMap[y][x]['unit'].rangeMax == 1: #if units range is only 1
        if x + 1 <= mapWidth - 1:
            if gameMap[y][x + 1]['unit'] != None:
                if gameMap[y][x + 1]['unit'].team != gameMap[y][x]['unit'].team and gameMap[y][x + 1]['unit'].unitClass in gameMap[y][x]['unit'].validAttacks:
                    selectedUnitAttacks.append((x + 1, y))
                    if not "attack" in selectedUnitOptions:
                        selectedUnitOptions.append("attack")
        if x - 1 >= 0:
            if gameMap[y][x - 1]['unit'] != None:
                if gameMap[y][x - 1]['unit'].team != gameMap[y][x]['unit'].team and gameMap[y][x - 1]['unit'].unitClass in gameMap[y][x]['unit'].validAttacks:
                    selectedUnitAttacks.append((x - 1, y))
                    if "attack" not in selectedUnitOptions:
                        selectedUnitOptions.append("attack")
        if y + 1 <= mapHeight - 1:
            if gameMap[y + 1][x]['unit'] != None:
                if gameMap[y + 1][x]['unit'].team != gameMap[y][x]['unit'].team and gameMap[y + 1][x]['unit'].unitClass in gameMap[y][x]['unit'].validAttacks:
                    selectedUnitAttacks.append((x, y + 1))
                    if "attack" not in selectedUnitOptions:
                        selectedUnitOptions.append("attack")
        if y - 1 >= 0:
            if gameMap[y - 1][x]['unit'] != None:
                if gameMap[y - 1][x]['unit'].team != gameMap[y][x]['unit'].team and gameMap[y - 1][x]['unit'].unitClass in gameMap[y][x]['unit'].validAttacks:
                    selectedUnitAttacks.append((x, y - 1))
                    if "attack" not in selectedUnitOptions:
                        selectedUnitOptions.append("attack")
    else: #if units have a range more than 1
        maximum = gameMap[y][x]['unit'].rangeMax
        minimum = gameMap[y][x]['unit'].rangeMin
        for yy in range(mapHeight):
            for xx in range(mapWidth):
                if calculateMoveDistance(x, y, xx, yy) >= minimum and calculateMoveDistance(x, y, xx, yy) <= maximum:
                    if gameMap[yy][xx]['unit'] != None:
                        if gameMap[yy][xx]['unit'].team != gameMap[y][x]['unit'].team and gameMap[yy][xx]['unit'].unitClass in gameMap[y][x]['unit'].validAttacks:
                            selectedUnitAttacks.append((xx, yy))
                            if "attack" not in selectedUnitOptions:
                                selectedUnitOptions.append("attack")
    selectedUnitOptions.append("wait")


def moveSelectedUnit(mapX, mapY):
    global selectedUnit, gameMap
    y, x = selectedUnit
    unit = gameMap[y][x]['unit']
    gameMap[y][x]['unit'] = None
    gameMap[mapY][mapX]['unit'] = unit


def reactivateUnits():
    global gameMap
    for row in gameMap:
        for column in row:
            if column["unit"] != None:
                if not column["unit"].active:
                    column["unit"].active = True

    
def mouseWasClicked(mousePos, button):
    global menuOn, drawOptions, selectedUnit, selectedUnitMap, menuCorner, selectedUnitAttacks, attackOn, turn
    global scrollOffsetX, scrollOffsetY
    global mapBoxSize, gameMap, windowDimensions
    if not menuOn:
        # Calculate Where the User Clicked on the Map
        x, y = mousePos
        x += scrollOffsetX
        y += scrollOffsetY
        # Calculate which grid square they clicked on
        mapX = x // mapBoxSize
        mapY = y // mapBoxSize
        # Make sure they clicked on the map
        if not mapX <= mapWidth - 1 or not mapY <= mapHeight - 1:
            return 
        global highlightedSquares, checkedSquares
        if selectedUnit == None:
            if gameMap[mapY][mapX]["unit"] != None and gameMap[mapY][mapX]["unit"].active:
                if gameMap[mapY][mapX]["unit"].team == turn:
                    if button == 1:
                        # Unit has been selected.  Set selectedUnit variable so draw function will draw available moves
                        selectedUnit = (mapY, mapX)
                        generateSelectedUnitRadar()
        else: # A unit has already been selected
            y, x = selectedUnit
            if (mapY, mapX) in highlightedSquares and (gameMap[mapY][mapX]['unit'] == None or (mapX == x and mapY == y)):
                # The square the user clicked on is a valid move so move unit and give available options
                moveSelectedUnit(mapX, mapY)
                selectedUnitMap = (mapX, mapY)
                menuOn = True
                # give draw function information to draw the unit's options
                # which corner should the options be drawn in?
                menuCorner = 1
                if calculateMoveDistance(mapX, mapY, 0, 0) < 5:
                    menuCorner = 2
                    xx, yy = windowDimensions
                # which options does the unit have?
                generateSelectedUnitOptions(mapX, mapY)
                global selectedUnitOptions
                # drawOptions = [[Rect Height, Rect Width, Rect Center], for each option - [Option Text, Option Position]]
                width = 100
                height = 75 + (50 * len(selectedUnitOptions))
                if menuCorner == 1:
                    center = (width / 2, height / 2)
                elif menuCorner == 2:
                    center = (xx - width / 2, yy - height / 2)
                drawOptions = []
                drawOptions.append([height, width, center])
                if menuCorner == 1:
                    for i in range(len(selectedUnitOptions)):
                        xxx = 0
                        yyy = (i + 1) * 50
                        drawOptions.append([selectedUnitOptions[i], (xxx, yyy)])
                else:
                    for i in range(len(selectedUnitOptions)):
                        xxx = xx - width
                        yyy = yy - ((i + 1) * 50) - 25
                        drawOptions.append([selectedUnitOptions[i], (xxx, yyy)])
                # Unit was moved so clear highlightedSquares variable
                highlightedSquares = []
                # checkedSquares needs to be cleared because it is vital to calculating highlightedSquares
                checkedSquares = []
            else: # The square the user clicked on is not a valid move so the unit is no longer selected and will not be moved anywhere
                selectedUnit = None
                highlightedSquares = []
                checkedSquares = []
    elif attackOn:
        x, y = mousePos
        x += scrollOffsetX
        y += scrollOffsetY
        # Calculate which grid square they clicked on
        mapX = x // mapBoxSize
        mapY = y // mapBoxSize
        for option in selectedUnitAttacks:
            if option == (mapX, mapY):
                x, y = selectedUnitMap
                gameMap[y][x]['unit'].attack(gameMap[mapY][mapX]['unit'])
                gameMap[y][x]['unit'].active = False
                menuOn = False
                attackOn = False
                drawOptions = None
                selectedUnit = None
                selectedUnitMap = None
                highlightedSquares = []
                checkedSquares = []
                selectedUnitAttacks = []
                return
        # User did not click on a valid attack spot
        #move unit back to original position
        x, y = selectedUnitMap
        ys, xs = selectedUnit
        unit = gameMap[y][x]['unit']
        gameMap[y][x]['unit'] = None
        gameMap[ys][xs]['unit'] = unit
        menuOn = False
        attackOn = False
        drawOptions = None
        selectedUnit = None
        selectedUnitMap = None
        highlightedSquares = []
        checkedSquares = []
        selectedUnitAttacks = []
    else: # Menu is currently on
        y, x = selectedUnit
        xmap, ymap = selectedUnitMap
        mouseX, mouseY = mousePos
        clickedOption = None
        if menuCorner == 1:
            if mouseX >= 0 and mouseX <= 100:
                clickedOption = (mouseY - (75/2)) // 50
        else:
            xx, yy = windowDimensions
            if mouseX <= xx and mouseX >= xx - 100:
                clickedOption = ((yy - mouseY) - (75/2)) // 50
        if clickedOption == None or clickedOption >= len(selectedUnitOptions): #no option is clicked
            #move unit back to original position
            unit = gameMap[ymap][xmap]['unit']
            gameMap[ymap][xmap]['unit'] = None
            gameMap[y][x]['unit'] = unit
        elif selectedUnitOptions[clickedOption] == "wait":
            gameMap[ymap][xmap]['unit'].active = False
        elif selectedUnitOptions[clickedOption] == "attack":
            attackOn = True
            return
        menuOn = False
        drawOptions = None
        selectedUnit = None
        selectedUnitMap = None
        highlightedSquares = []
        checkedSquares = []
        selectedUnitAttacks = []

    # global selectedUnit
    # if gameMap[mapY][mapX]["unit"] != None:
    #     if button == 1:
    #         selectedUnit = gameMap[mapY][mapX]["unit"]
    #     elif button == 3:
    #         selectedUnit.attack(gameMap[mapY][mapX]["unit"])


def checkMap():
    global gameMap
    # Check Map for units with 0 hp and destroy them!
    for row in gameMap:
        for column in row:
            if column["unit"] != None:
                if column["unit"].hp <= 0:
                    column["unit"] = None


initGame()
while True:
    beginningLoopStuff()
    calculateScrolling()
    draw()
    checkEvents()
    checkMap()
    endLoopStuff()