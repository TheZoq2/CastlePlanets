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
            pos += Vec2((SCREEN_WIDTH - 300) / 2, (SCREEN_HEIGHT - 200) / 2)

            v1 = pos + Vec2(img.get_width(), img.get_height())
            v2 = Vec2(SCREEN_WIDTH, SCREEN_HEIGHT)
            if v1.x < 0 or v1.y < 0 or pos.x > v2.x or pos.y > v2.y:
                return
            pos -= Vec2(img.get_width() / 2, img.get_height() / 2)

            self.screen.blit(img, (pos.x, pos.y))

    def line(self, start, end):
        start -= self.camera
        end -= self.camera
        start += Vec2((SCREEN_WIDTH - 300) / 2, (SCREEN_HEIGHT - 200) / 2)
        end += Vec2((SCREEN_WIDTH - 300) / 2, (SCREEN_HEIGHT - 300) / 2)
        pygame.draw.line(self.screen, (255, 255, 255), (start.x, start.y), (end.x, end.y))

