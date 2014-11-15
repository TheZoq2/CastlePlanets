import pygame
from Vec2 import *

planetImgs = [pygame.image.load("planet.png")]

class Planet:
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type

    def get_coords(self):
        return self.pos

    def draw(self, renderer):
        renderer.draw(planetImgs[self.type], self.pos)

