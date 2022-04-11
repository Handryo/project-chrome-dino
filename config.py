import pygame

pygame.mixer.init()
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

# Collisions
obstacles_group = pygame.sprite.Group()
collision = False

# Score
score = 0

# Velocity
cloud_vel = 4
game_vel = 10


# Sounds
class Sounds:
    jump_sound = pygame.mixer.Sound("sound/jump_sound.wav")
    jump_sound.set_volume(1)
    score_sound = pygame.mixer.Sound("sound/score_sound.wav")
    score_sound.set_volume(1)
    death_sound = pygame.mixer.Sound("sound/death_sound.wav")
    death_sound.set_volume(1)
