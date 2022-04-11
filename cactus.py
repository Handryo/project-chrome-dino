import pygame.sprite
from random import randrange
from config import sprite_cactus, width, height, game_vel


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_cactus = []
        for s in range(7):
            img = sprite_cactus.subsurface((s * 34, 0), (34, 34))
            img = pygame.transform.scale(img, (34 * 2, 34 * 2))
            self.image_cactus.append(img)
        self.index_list = 0
        self.image = self.image_cactus[self.index_list]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (width, height - 64)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = width
            self.index_list = randrange(0, 7, 1)
            self.rect.x = randrange(640, 1000, 45)
        self.image = self.image_cactus[self.index_list]
        self.rect.x -= game_vel
