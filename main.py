import pygame

from pygame import mixer

# Init the game
pygame.init()

#screen resolution &  game params
WIDTH = 1400
HEIGHT = 800
FPS = 60
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load('assets/maps/level0.png')
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

# Sounds & Background Music
mixer.music.load('assets/sounds/medieval.ogg')
mixer.music.play(-1)

# Instancing the Hero
hero_image = pygame.image.load('assets/character/hero/Warrior/Individual Sprite/idle/Warrior_Idle_1.png')
hero_x = 50


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


#Sprites groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


#Game loop

running = True
while   running :
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Player Input Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        hero_x -= 2
    if keys[pygame.K_d]:
        hero_x += 2
    if keys[pygame.K_z]:
        ...
    if keys[pygame.K_s]:
        ...


    #Update
    all_sprites.update()

    # Draw / render / Background
    screen.fill(BLACK)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(hero_image,(hero_x,690))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.display.update()
