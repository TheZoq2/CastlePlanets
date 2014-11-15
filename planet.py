import pygame
from Vec2 import *

planetImgs = [pygame.image.load("planet.png")]

class Planet:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def get_image(self):
        return planetImgs[self.type]

    def get_coords(self):
        return Vec2(self.x, self.y)
