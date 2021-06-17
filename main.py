
import pygame

#screen resolution &  game params

WIDTH = 1400
HEIGHT = 800
FPS = 60
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Title and Icon
pygame.display.set_caption("    ▬▬ι═══════>         ▂▃▅▇█▓▒░۩۞۩      Tales  Of  Swan       ۩۞۩░▒▓█▇▅▃▂       <═══════ι▬▬      ")
icon = pygame.image.load('assets/gameui/sword.png')
pygame.display.set_icon(icon)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

#Sprites groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Init the game
pygame.init()

#Game loop

running = True
while   running :
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.display.update()
