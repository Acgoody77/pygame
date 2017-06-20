import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

object_width = 120
"""
game
"""

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

duckImg = pygame.image.load('images/duck.png')
rifle_man = pygame.image.load('images/rifle.png')

def putImg(file_name,x,y):
    gameDisplay.blit(file_name, (x,y))

def text_objects(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()

def message_display(text):
    font_text = pygame.font.Font('freesansbold.ttf', 50)
    text_surf, text_rect = text_objects(text, font_text)
    text_rect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(text_surf, text_rect)

    pygame.display.update()

    #time.sleep(2)

    #game_loop()

def crash():
    message_display("crashed")

def game_loop():
    x = (display_width * .45)
    y = (display_height * .8)

    key_left = False
    key_right = False
    key_up = False
    key_down = False
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                gameExit = True


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key_left = True
                elif event.key == pygame.K_RIGHT:
                    key_right = True
                elif event.key == pygame.K_UP:
                    key_up = True
                elif event.key == pygame.K_DOWN:
                    key_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    key_left = False

                if event.key == pygame.K_RIGHT:
                    key_right = False

                if event.key == pygame.K_UP:
                    key_up = False

                if event.key == pygame.K_DOWN:
                    key_down = False




        gameDisplay.fill(black)
        #putImg(duckImg,x,y)
        putImg(rifle_man, x, y)

        if key_left == True and x > 0:
            x -= 5
            message_display("left")
        if key_right == True and x < (display_width - 96):
            x += 5
            message_display("right")
        if key_up == True and y > 0:
            y -= 5
            message_display("up")
        if key_down == True and y < (display_height - 124):
            y += 5
            message_display("down")

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
