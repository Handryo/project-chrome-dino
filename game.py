from pygame import *
from cactus import *
from cloud import *
from config import *
from dino import *
from floor import *
from mensages import *
from dino_fly import *


class Game:
    def __init__(self):
        pass
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dino run")

    Dino = Dino(sprite_dino)
    Messages = Messages()

    game_over = Messages.show_text('GAME OVER', 35, black)
    close = Messages.show_text('Press "x" to close the Game', 20, black)

    for ct in range(2):
        cactus = Cactus()
        all_sprites.add(cactus)
        obstacles_group.add(cactus)

    for c in range(4):
        cloud = Cloud(sprite_cloud)
        all_sprites.add(cloud)

    for f in range(640 * 2 // 64):
        floor = Floor(f, sprite_floor)
        all_sprites.add(floor)

    dino_fly = Ptera(sprite_dino_fly)
    all_sprites.add(dino_fly)
    obstacles_group.add(dino_fly)

    collision = False
    while True:
        clock.tick(30)
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if dino.rect.y == 508 and not collision:
                        Sounds.jump_sound.play()
                        dino.leap()
                if event.key == pygame.K_x and collision:
                    exit()

        if key.get_pressed()[K_DOWN]:
            dino.duck()
        else:
            if dino.down:
                dino.undunking()

        collisions = pygame.sprite.spritecollide(dino, obstacles_group, False, pygame.sprite.collide_mask)
        all_sprites.draw(screen)
        if collisions and not collision:
            Sounds.death_sound.play()
            collision = True

        if collision:
            dino.dead()
            screen.blit(game_over, (width // 2 - 150, height // 2 - 150))
            screen.blit(close, (width // 2 - 260, height // 2 - 90))
            score_dino2 = Messages.show_text(score, 35, black)
            screen.blit(score_dino2, (520, 30))
        else:
            score += 1
            score_dino = Messages.show_text(score, 35, black)
            screen.blit(score_dino, (520, 30))
            all_sprites.update()
        if score % 100 == 0:
            Sounds.score_sound.play()
        pygame.display.flip()
