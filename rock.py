from configs import *
from random import *
import pygame


class Rock:
    def __init__(self):
        self.__skin = None
        self.__x = None
        self.__y = 280
        self.__speed = 2

        self.reset()

    def get_x(self):
        return self.__x

    def reset(self, last_rock_ref=None):
        self.__skin = choice(list(Skin.rocks.values()))

        final_x = 0
        if last_rock_ref:
            final_x = last_rock_ref.get_x()
            if final_x < window.WIDTH:
                final_x = window.WIDTH
        else:
            final_x = window.WIDTH

        self.__x = final_x + randint(20, 50)

    def move(self):
        self.__x -= self.__speed

    def is_out(self):
        return self.__x < -self.__skin.get_width()

    def draw(self):
        surface = pygame.display.get_surface()
        surface.blit(self.__skin, [self.__x, self.__y])

    @classmethod
    def creat_group(cls, quant):
        rocks_list = []
        for _ in range(quant):
            rocks_list.append(Rock())

        return rocks_list
