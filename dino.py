import pygame.sprite
from config import sprite_dino


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_dino = []
        for i in range(3):
            img = sprite_dino.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*2, 32*2))
            self.image_dino.append(img)
        self.index_list = 0
        self.image = self.image_dino[self.index_list]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 500)

    def update(self):
        if self.index_list > 2:
            self.index_list = 1
        self.index_list += 0.25
        self.image = self.image_dino[int(self.index_list)]


all_sprites = pygame.sprite.Group()
dino = Dino()
all_sprites.add(dino)
