import pygame.sprite
from config import width, cloud_vel
from random import randrange


class Cloud(pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite
        self.image = pygame.transform.scale(sprite, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.x = width - randrange(30, 400, 50)
        self.rect.y = randrange(50, 400, 50)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = width
            self.rect.y = randrange(50, 400, 50)
        self.rect.x -= cloud_vel
        
