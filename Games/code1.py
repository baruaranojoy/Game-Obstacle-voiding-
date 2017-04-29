import pygame
import time
import random

pygame.init()

display_width = 900
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width , display_height))
pygame.display.set_caption('Avoid Them')
clock = pygame.time.Clock()

carImg = pygame.image.load('car6.png')

def things(thingx , thingy , thingw , thingh , color):
    pygame.draw.rect(gameDisplay , color , [thingx, thingy, thingw, thingh])


def car(x,y):
    gameDisplay.blit(carImg, (x,y))


def text_objects(text , font):
    textSurface = font.render(text , True , black)
    return textSurface , textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',120)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width/2 , display_height/2)
    gameDisplay.blit(TextSurf , TextRect)

    pygame.display.update()
    time.sleep(5)

    game_loop()

def crash():
    message_display('You Crashed !!')


def game_loop():
    x = (display_width * 0.42)
    y = (display_height * 0.70)

    x_change = 0
    y_change = 0

    car_width = 120
    
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 80
    thing_height = 100
    
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                chashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key == pygame.K_UP:
                    y_change = -3
                elif event.key == pygame.K_DOWN:
                    y_change = 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
            

        x = x + x_change
        y = y + y_change
            
        gameDisplay.fill(white)

        things(thing_startx , thing_starty , thing_width , thing_height , black)
        thing_starty = thing_starty + thing_speed
        
        car(x,y)

        if x > (display_width - 120) or x < -5:
            crash()
            
        if y < 1 or y >(display_height - 200):
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0 , display_width)

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width :
                crash()
                
        
        pygame.display.update()

        clock.tick(45)

game_loop()
pygame.quit()
quit()

    


    
