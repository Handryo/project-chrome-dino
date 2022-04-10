from config import *
from floor import *
from dino import *
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino run")

#for i in range(width * 3 // 96):
    #chao_ = Floor(chao_1, i)
    #todas_as_sprites.add(chao_)

Dino = Dino()

while True:
    clock.tick(30)
    screen.fill(white)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    all_sprites.draw(screen)
    all_sprites.update()
    #todas_as_sprites.draw(tela)
    #todas_as_sprites.update()
    pygame.display.flip()


