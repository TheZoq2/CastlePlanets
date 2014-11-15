import pygame
from Vec2 import *

planetImgs = [pygame.image.load("planet.png")]

class Planet:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def draw(self, renderer):
        renderer.draw(planetImgs[self.type], Vec2(self.x, self.y))

