import pygame.display
from configs import *
from enumeration import *
from bullet import *

shots = []


class Player:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__skin = Skin.pig
        self.__life = 5
        self.__jumping_state = None
        self.__jump_frames = 0
        self.__gravity = 0
        self.__cooldown = 0

    def get_position(self):
        return self.__x, self.__y

    def draw(self):
        surface = pygame.display.get_surface()
        surface.blit(self.__skin, [self.__x, self.__y])

    def jump(self):
        self.__jumping_state = Direction.RISING

    def update_jump(self):
        if not self.__jumping_state:
            return

        if self.__jumping_state == Direction.RISING:
            if self.__gravity > 0:
                self.__gravity -= 1

            self.__y -= 5 + self.__gravity
        elif self.__jumping_state == Direction.FALLING:
            if self.__gravity < 15:
                self.__gravity += 2

            self.__y += 5 + self.__gravity

        if self.__y < 100 or self.__y > 215:
            if self.__jumping_state == Direction.RISING:
                self.__jumping_state = Direction.FALLING
                self.__y = 100
                self.__gravity = 0
            elif self.__jumping_state == Direction.FALLING:
                self.__jumping_state = None
                self.__y = 215
                self.__gravity = 15

    def move(self, direction):
        if direction == Direction.LEFT:
            self.__x -= 10
        elif direction == Direction.RIGHT:
            self.__x += 10

        if self.__x < 15:
            self.__x = 15
        elif self.__x > window.WIDTH - self.__skin.get_width() - 15:
            self.__x = window.WIDTH - self.__skin.get_width() - 15

    def shoot(self, bullet):
        if self.__cooldown >= 10:
            self.__cooldown = 0
            return

        elif self.__cooldown < 10:
            bullet = Bullet()
            shots.append(bullet)
            bullet.set_fired([self.__x + 30, self.__y])

    def set_cooldown(self):
        self.__cooldown += 1
