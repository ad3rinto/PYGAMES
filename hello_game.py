# Simple Python game

# import and initialize the pygame module

import pygame
pygame.init()

# set up the drawing window

screen = pygame.display.set_mode((500, 500))

# run until user asks to quit

running = True
while running:
    # did the user click the close buttom?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the background with white
    screen.fill((255, 255, 255))

    # draw a solid blue circle in the centre
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # flip the display
    pygame.display.flip()

    # DOne. time to end the game
pygame.quit()


