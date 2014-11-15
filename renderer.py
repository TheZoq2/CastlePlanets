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

    def draw(self, img, pos, isgui = False):
        if isgui:
            self.screen.blit(img, (pos.x, pos.y))
        else:
            pos -= self.camera
            pos += Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            pos -= Vec2(img.get_width() / 2, img.get_height() / 2)
            self.screen.blit(img, (pos.x, pos.y))

