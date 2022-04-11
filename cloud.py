import pygame.sprite
from config import sprite_cloud, width
from random import randrange


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = sprite_cloud
        self.image = pygame.transform.scale(img, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.x = width - randrange(30, 400, 50)
        self.rect.y = randrange(50, 400, 50)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = width
            self.rect.y = randrange(50, 400, 50)
        self.rect.x -= 4
        
