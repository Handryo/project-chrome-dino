from pygame import *
from cloud import *
from config import *
from dino import *
from floor import *

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino run")

Dino = Dino()

for c in range(4):
    cloud = Cloud()
    all_sprites.add(cloud)

for f in range(640 * 2 // 64):
    floor = Floor(f)
    all_sprites.add(floor)

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

    if key.get_pressed()[K_DOWN]:
        dino.duck()
    else:
        if dino.down:
            dino.undunking()

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
