from pygame import *
from cactus import *
from cloud import *
from config import *
from dino import *
from floor import *
from mensages import *


def restart_game():
    cactus.rect.x = width
    

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino run")

Dino = Dino()
Mensages = Mensages()

for cact in range(2):
    cactus = Cactus()
    all_sprites.add(cactus)
    obstacles_group.add(cactus)

for c in range(4):
    cloud = Cloud()
    all_sprites.add(cloud)

for f in range(640 * 2 // 64):
    floor = Floor(f)
    all_sprites.add(floor)

colision = False
while True:
    clock.tick(30)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if dino.rect.y != 508:
                    pass
                else:
                    dino.leap()
                if event.key == K_r and colision == True:
                    restart_game()

    if key.get_pressed()[K_DOWN]:
        dino.duck()
    else:
        if dino.down:
            dino.undunking()

    colisions = pygame.sprite.spritecollide(dino, obstacles_group, False, pygame.sprite.collide_mask)
    all_sprites.draw(screen)
    if colisions and colision == False:
        colision = True

    if colision:
        dino.dead()
        game_over = Mensages.show_text('GAME OVER', 35, black)
        screen.blit(game_over, (width // 2 - 150, height // 2 - 150))
        restart = Mensages.show_text('Press "r" to restart', 20, black)
        screen.blit(restart, (width // 2 - 200, height // 2 - 90))
    else:
        all_sprites.update()
    pygame.display.flip()
