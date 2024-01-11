from configs import *
from enumeration import *
from random import *
import pygame


class Enemy:
    def __init__(self):
        self.__skin = None
        self.__x = None
        self.__y = None
        self.__speed = None
        self.__state = State.ALIVE

        self.reset()

    def reset(self):
        self.__skin = choice(list(Skin.enemies.values()))
        self.__x = window.WIDTH - (self.__skin.get_width() + randint(50, 200))
        self.__y = randint(10, 60)
        self.__speed = 3
        self.__state = State.ALIVE

    def move(self):
        self.__x -= self.__speed

        if self.__x <= 0:
            self.reset()

    def draw(self):
        surface = pygame.display.get_surface()
        surface.blit(self.__skin, [self.__x, self.__y])

    @classmethod
    def create_group(cls, quant):
        enemies_list = []
        for _ in range(quant):
            enemies_list.append(Enemy())

        return enemies_list
