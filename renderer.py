import pygame
from Vec2 import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 700

class Renderer:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.camera = Vec2(0, 0)

    def move_camera(self, vec):
        self.camera += vec

    def clear(self):
        self.screen.fill((0, 0, 0))

    def draw(self, obj):
        pos = obj.get_coords() - self.camera
        img = obj.get_image()
        self.screen.blit(img, (pos.x, pos.y))

