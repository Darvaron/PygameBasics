# Basics of pygame part 1

import pygame
import time
import random

pygame.init()  # Initiate pygame modules

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("music.wav")

display_width = 1366
display_height = 768

# Colors RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
block_color = (53, 115, 255)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))  # Window
pygame.display.set_caption('Test game')  # Change the name
clock = pygame.time.Clock()  # Define clock

car_width = 47

carImg = pygame.image.load('car.png')
carIcon = pygame.image.load("icon.png")
pygame.display.set_icon(carIcon)

pause = False


def thing_dodge(count):  # count the blocks dodged
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):  # Draw things, x,y pos, w,h size
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))  # Draw


def text_objects(text, font):
    TextSurface = font.render(text, True, black)  # Anti-aliasing is the True value
    return TextSurface, TextSurface.get_rect()


def message_display(text):  # Display message
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('You Crashed')


def button(message, x, y, w, h, ico, aco, act=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # Button ilussion
        pygame.draw.rect(gameDisplay, ico, (x, y, w, h))
        if click[0] == 1 and act != None:
            act()  # Run act
    else:
        pygame.draw.rect(gameDisplay, aco, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(message, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():  # Separate sequence

    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Paused', largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button('Continue', 400, 500, 100, 50, green, bright_green, unpause)
        button('Quit', 850, 500, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():  # Separate sequence
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Test game', largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button('Lets go', 400, 500, 100, 50, green, bright_green, game_loop)
        button('Quit', 850, 500, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    pygame.mixer.music.play(-1) #-1 is infinite loop
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:  # Making a loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed

        car(x, y)
        thing_dodge(dodged)

        if x > display_width - car_width or x < 0:  # Boundaries
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:  # collision

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()

        pygame.display.update()  # Updates only the parameter, if don't it updates all
        clock.tick(144)  # Frames per second


game_intro()
