import pygame
import os

pygame.font.init()

windowWidth = 500
cellWidth = 10
menuBarHeight = 100
myWindow = pygame.display.set_mode((windowWidth, windowWidth + menuBarHeight))
myIcon = pygame.image.load(os.path.join("../Assets", "Icon.png")).convert_alpha()
myFont = pygame.font.Font("../Assets/PixeloidMono-1G8ae.ttf", 20)
myFontSmall = pygame.font.Font("../Assets/PixeloidMono-1G8ae.ttf", 15)
textColor1 = 'gold'
textColor2 = 'white'
myClock = pygame.time.Clock()
fps = 120