import pygame
import pygame.sprite
from config import sprite_dino, all_sprites

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_dino = []
        for i in range(5):
            img = sprite_dino.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 2, 32 * 2))
            self.image_dino.append(img)
        self.index_list = 0
        self.image = self.image_dino[self.index_list]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 508
        self.jump = False
        self.down = False

    def leap(self):
        self.jump = True

    def duck(self):
        self.down = True

    def undunking(self):
        self.down = False

    def update(self):
        # Dino leap
        if self.jump:
            if self.rect.y <= 300:
                self.jump = False
            self.rect.y -= 20
        else:
            if self.rect.y < 508:
                self.rect.y += 20
            else:
                self.rect.y = 508
        # Dino duck
        if self.down:
            if self.index_list > 4:
                self.index_list = 3
            self.index_list += 0.25
            self.image = self.image_dino[int(self.index_list)]

        # Dino run
        if not self.down:
            if self.index_list > 2:
                self.index_list = 1
            self.index_list += 0.25
            self.image = self.image_dino[int(self.index_list)]


dino = Dino()
all_sprites.add(dino)
