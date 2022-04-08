
from config import *
from chao import todas_as_sprites
pygame.init()
tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption("Frog Adventure")

while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()

