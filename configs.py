import pygame

class window:
    WIDTH = 600
    HEIGH = 338
    TITLE = "Hunter Day"
    icon = pygame.image.load("imgs/icon.png")


class Skin:
    # Main skins
    background = pygame.image.load("imgs/Background.png")
    bullet = pygame.image.load("imgs/bullet.png")
    pig = pygame.image.load("imgs/pig.png")
    rocks = {
        "rock1": pygame.image.load("imgs/rock1.png"),
        "rock2": pygame.image.load("imgs/rock2.png"),
        "rock3": pygame.image.load("imgs/rock3.png")
    }

    enemies = {
        "blue": pygame.image.load("imgs/enemies/blue.png"),
        "green": pygame.image.load("imgs/enemies/green.png"),
        "orange": pygame.image.load("imgs/enemies/orange.png"),
        "red": pygame.image.load("imgs/enemies/red.png"),
        "white": pygame.image.load("imgs/enemies/white.png"),
        "yellow": pygame.image.load("imgs/enemies/yellow.png")
    }