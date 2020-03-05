# Basics of pygame part 2

import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)

#Pixel
pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

#Line
pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)

#Rectangle
pygame.draw.rect(gameDisplay, red, (400,400,50,25))

#Circle
pygame.draw.circle(gameDisplay, white, (150,150), 75)

#polygon
pygame.draw.polygon(gameDisplay, green, ((25, 75), (76, 125), (250, 375), (400, 25), (60, 540)))#Connect the dots in the exact order

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()