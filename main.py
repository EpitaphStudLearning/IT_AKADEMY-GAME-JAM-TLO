# Init the game
import pygame

pygame.init()

#screen resolution

screen = pygame.display.set_mode((1400,800))


# Title and Icon
pygame.display.set_caption("    ▬▬ι═══════>         ▂▃▅▇█▓▒░۩۞۩      Tales  Of  Swan       ۩۞۩░▒▓█▇▅▃▂       <═══════ι▬▬      ")
icon = pygame.image.load('assets/gameui/sword.png')
pygame.display.set_icon(icon)


#Game loop

running = True
while   running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

