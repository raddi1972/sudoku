import pygame
import final
import sys
import os

# initializing the constructor
pygame.init()


# screen resolution
res = (620, 400)

screen1 = pygame.display.set_mode(res)
image1 = pygame.image.load(os.path.join('img', 'h.jpeg'))
image2 = pygame.image.load(os.path.join('img', 'e2.jpeg'))
image3 = pygame.image.load(os.path.join('img', 'img64.jpeg'))
# white color
color1 = (255, 255, 255)

# light shade of the button
color_light1 = (170, 170, 170)

# dark shade of the button
color_dark1 = (100, 100, 100)

width = screen1.get_width()

height = screen1.get_height()

# defining a font
smallfont = pygame.font.SysFont('italic', 35)

text1 = smallfont.render('START ', True, color1)

text2 = smallfont.render('INSTRUCTIONS ', True, color1)

text3 = smallfont.render('QUIT ', True, color1)

text4 = smallfont.render('Home', True, color1)


def instructions():

    while True:

        for event1 in pygame.event.get():

            if event1.type == pygame.QUIT:
                pygame.quit()
                exit()

            screen1.blit(image3, (0, 0))

            pygame.draw.rect(screen1, (196, 164, 132), pygame.Rect(
                width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40))

            if event1.type == pygame.MOUSEBUTTONDOWN:
                # to quit
                if width / 2 + width / 4 - 5 <= mouse[0] <= width / 2 + width / 4 - 5+90 and height / 2 + 140 - 3 <= mouse[1] <= height / 2 + 140 - 3 + 38:
                    start()

            mouse = pygame.mouse.get_pos()

            if width / 2 + width / 4 - 5 <= mouse[0] <= width / 2 + width / 4 - 5 + 90 and height / 2 + 140 - 3 <= mouse[1] <= height / 2 + 140 - 3 + 40:
                pygame.draw.rect(screen1, (255, 164, 132), pygame.Rect(
                    width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40))

            screen1.blit(text4, (width / 2 + width / 4, height / 2 + 140))
            pygame.display.update()


def start():

    while True:

        screen1.blit(image2, (0, 0))

        pygame.draw.rect(screen1, (196, 164, 132), pygame.Rect(
            width / 2 - width / 4 - 80, height / 2 + 20, 120, 50))
        pygame.draw.rect(screen1, (196, 164, 132), pygame.Rect(
            width / 2 - 100 - 10, height / 2 + 80, 250, 50))
        pygame.draw.rect(screen1, (196, 164, 132), pygame.Rect(
            width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40))

        for event1 in pygame.event.get():

            if event1.type == pygame.QUIT:
                pygame.quit()
                exit()

                # checks if a mouse is clicked
            if event1.type == pygame.MOUSEBUTTONDOWN:
                # to quit
                if width / 2 + width / 4 - 5 <= mouse[0] <= width / 2 + width / 4 - 5+90 and height / 2 + 140 - 3 <= mouse[1] <= height / 2 + 140 - 3 + 38:
                    pygame.quit()
                    exit()

                elif width / 2 - 100 - 10 <= mouse[0] <= width / 2 - 100 - 10+250 and height / 2 + 80 <= mouse[1] <= height / 2 + 80 + 50:
                    instructions()

                elif width / 2 - width/4-80 <= mouse[0] <= width / 2 - width/4-80+120 and height / 2+20 <= mouse[1] <= height / 2 + 70:
                    final.begin()
                else:
                    pygame.display.update()

        # save the (x,y) coordinates into

        mouse = pygame.mouse.get_pos()

        # if mouse  on a button
        #  to change to lighter shade
        if width / 2 - width/4-80 <= mouse[0] <= width / 2 - width/4-80+120 and height / 2+20 <= mouse[1] <= height / 2 + 70:
            pygame.draw.rect(screen1, (255, 164, 132), pygame.Rect(
                width / 2 - width / 4 - 80, height / 2 + 20, 120, 50))

        if width / 2 - 100 - 10 <= mouse[0] <= width / 2 - 100 - 10+250 and height / 2 + 80 <= mouse[1] <= height / 2 + 80 + 50:
            pygame.draw.rect(screen1, (255, 164, 132), pygame.Rect(
                width / 2 - 100 - 10, height / 2 + 80, 250, 50))

        if width / 2 + width / 4 - 5 <= mouse[0] <= width / 2 + width / 4 - 5 + 90 and height / 2 + 140 - 3 <= mouse[1] <= height / 2 + 140 - 3 + 40:
            pygame.draw.rect(screen1, (255, 164, 132), pygame.Rect(
                width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40))

            #  the text onto our button
        screen1.blit(text1, (width / 2 - width/4-70, height / 2+30))
        screen1.blit(text2, (width / 2-100, height / 2+90))
        screen1.blit(text3, (width / 2 + width/4, height / 2+140))

        # updates the frames of the game
        pygame.display.update()


start()
