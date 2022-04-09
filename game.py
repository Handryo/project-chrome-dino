
from config import *
from chao import *
pygame.init()
tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption("Frog Adventure")

todas_as_sprites = pygame.sprite.Group()
for i in range(Largura * 3 // 96):
    chao_ = Chao(chao_1, i)
    todas_as_sprites.add(chao_)

while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()

