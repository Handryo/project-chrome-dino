import pygame.sprite
from config import width, height, sprite_floor

class Floor(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.image_floor = []
        for s in range(4):
            img = sprite_floor.subsurface((s * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 2, 32 * 2))
            self.image_floor.append(img)
        self.index_list = 0
        self.image = self.image_floor[self.index_list]
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x * 64
        self.rect.y = height - 64

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = width
        self.rect.x -= 10
