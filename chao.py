import pygame.sprite
from config import Largura, Altura, chao1, chao2


class Chao(pygame.sprite.Sprite):
    def __init__(self, piso, pos_x):
        super().__init__()
        self.image = piso
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * 100
        self.rect.y = Altura - 84

    def update(self):
        self.rect.x = self.rect.x - 10
        if self.rect.x < - 100:
            self.rect.x = Largura


todas_as_sprites = pygame.sprite.Group()
for i in range(Largura * 2 // 100):
    chao_ = Chao(chao1, i)
    todas_as_sprites.add(chao_)



