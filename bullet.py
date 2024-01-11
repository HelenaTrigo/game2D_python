from configs import *
from player import *


class Bullet:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__speed = 4
        self.__skin = Skin.bullet
        self.__is_fired = False

    def set_fired(self, position):
            self.__is_fired = True
            self.__x = position[0] + 30
            self.__y = position[1]

    def move(self):
        if not self.__is_fired:
            return

        self.__y -= self.__speed

        if self.__y <= 0:
            self.__is_fired = False

    def draw(self):
        if not self.__is_fired:
            return

        surface = pygame.display.get_surface()
        surface.blit(self.__skin, [self.__x, self.__y])


