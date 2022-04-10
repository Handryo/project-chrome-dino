import pygame.sprite
from config import height, width


class Floor(pygame.sprite.Sprite):
    def __init__(self, floor, pos_x):
        super().__init__()
        self.ticks = None
        self.image = floor
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * 96
        self.rect.y = height - 96

    def update(self):
        self.ticks = pygame.time.get_ticks()
        self.rect.x = self.rect.x - 5
        if self.rect.x < -96:
            self.rect.x = width + 96
            
