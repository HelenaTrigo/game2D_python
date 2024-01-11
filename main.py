import pygame
from pygame.locals import *
from configs import *
from player import *
from enemy import *
from enumeration import *
from rock import *
from bullet import *


screen = pygame.display.set_mode([window.WIDTH, window.HEIGH])
pygame.display.set_icon(window.icon)
pygame.display.set_caption(window.TITLE)

pig1 = Player(250, 215)
enemies = Enemy.create_group(5)
rocks = Rock.creat_group(2)


clock = pygame.time.Clock()
while 1:
    dt = clock.tick(60)

    # eventos da janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(Skin.background, [0, 0])

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        pig1.move(Direction.LEFT)
    elif key[pygame.K_RIGHT]:
        pig1.move(Direction.RIGHT)

    if key[pygame.K_UP]:
        pig1.jump()

    if key[pygame.K_SPACE]:
        for bullet in shots:
            pig1.shoot(bullet)
            print(shots)
            bullet.move()
            bullet.draw()
            pig1.set_cooldown()

    pig1.update_jump()
    pig1.draw()

    for enemy in enemies:
        enemy.move()
        enemy.draw()

    for rock in rocks:
        rock.move()

        if rock.is_out():
            rock.reset(rocks[-1])

        rock.draw()

    pygame.display.update()
