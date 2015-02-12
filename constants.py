import pygame

background_colour = (255, 255, 255)
size = (800, 450)
black = (0, 0, 0)
scrollFactor = 20
gridWidth = 5

colors = {
    'darkRed': pygame.Color(127, 0, 0),
    'red': pygame.Color(255, 0, 0),
    'lightRed': pygame.Color(255, 127, 127),
    'darkGreen': pygame.Color(0, 127, 0),
    'green': pygame.Color(0, 255, 0),
    'lightGreen': pygame.Color(127, 255, 127),
    'darkYellow': pygame.Color(127, 127, 0),
    'yellow': pygame.Color(255, 255, 0),
    'lightYellow': pygame.Color(255, 255, 127),
    'darkBlue': pygame.Color(0, 0, 127),
    'blue': pygame.Color(0, 0, 255),
    'lightBlue': pygame.Color(127, 127, 255),
    'darkMagenta': pygame.Color(127, 0, 127),
    'magenta': pygame.Color(255, 0, 255),
    'lightMagenta': pygame.Color(255, 127, 255),
    'darkCyan': pygame.Color(0, 127, 127),
    'cyan': pygame.Color(0, 255, 255),
    'lightCyan': pygame.Color(127, 255, 255),
    'black': pygame.Color(0, 0, 0),
    'darkGrey': pygame.Color(64, 64, 64),
    'grey': pygame.Color(127, 127, 127),
    'white': pygame.Color(255, 255, 255)
}