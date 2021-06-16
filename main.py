# Init the game
import pygame

pygame.init()

#screen resolution

screen = pygame.display.set_mode((1400,800))

#Game loop

running = True
while   running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

