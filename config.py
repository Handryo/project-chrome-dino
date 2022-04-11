import pygame

width = 640
height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Sprites
sprite_dino = pygame.image.load("img/Dino.png")  # Dino
sprite_cloud = pygame.image.load("img/Cloud_sprite.png")  # Cloud
sprite_floor = pygame.image.load("img/Floor_sprite.png")  # Floor
sprite_cactus = pygame.image.load("img/Obstacle_Cactus.png")  # Cactus
all_sprites = pygame.sprite.Group()  # Add images to sprite group

# Colisions
obstacles_group = pygame.sprite.Group()
colision = False
