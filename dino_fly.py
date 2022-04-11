import pygame.sprite
from config import width


class Ptera(pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image_ptera = []
        self.sprite = sprite
        self.img1 = sprite.subsurface((0, 0), (32, 32))
        self.img2 = sprite.subsurface((32, 0), (32, 32))
        self.img_1 = pygame.transform.scale(self.img1, (32 * 2, 32 * 2))
        self.img_2 = pygame.transform.scale(self.img2, (32 * 2, 32 * 2))
        self.image_ptera.append(self.img_1)
        self.image_ptera.append(self.img_2)
        self.index_list = 0
        self.image = self.image_ptera[self.index_list]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (width, 300)

    def update(self):
        if self.rect.topright[0] < -1000:
            self.rect.x = width
        self.rect.x -= 8
        if self.index_list > 1:
            self.index_list = 0
        self.index_list += 0.25
        self.image = self.image_ptera[int(self.index_list)]
        pygame.display.update()
