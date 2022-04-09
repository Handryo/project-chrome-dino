import pygame.sprite
from config import Largura, Altura


class Chao(pygame.sprite.Sprite):
    def __init__(self, piso, pos_x):
        super().__init__()
        self.image = piso
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * 96
        self.rect.y = Altura - 96

    def update(self):
        ticks = pygame.time.get_ticks()
        self.rect.x = self.rect.x - 5
        if self.rect.x < -96:
            self.rect.x = Largura + 96
        print(ticks)

