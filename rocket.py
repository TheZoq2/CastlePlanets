import pygame, enum
from Vec2 import *

rocketImg = pygame.image.load("rocket.png")

class Dir(enum.IntEnum):
    away = 1
    back = -1

class Rocket:
    def __init__(self, planet):
        self.planet = planet
        self.route = None
        self.dir = Dir.away
        self.progress = 0
        self.speed = 0.5

    def update(self, dt):
        if self.route:
            self.progress += dt * self.speed
            if self.progress >= 1:
                self.progress = 0
                self.dir *= -1

    def get_image(self):
        return rocketImg

    def get_coords(self):
        if self.route == None:
            return self.planet.get_coords()
        else:
            p1 = self.route.path[0]
            p2 = self.route.path[1]

            difx = abs(p1.x - p2.x)
            dify = abs(p1.y - p2.y)

            if self.dir == Dir.away:
                pos = p1.x - difx * self.progress, p1.y + dify * self.progress
            else:
                pos = p2.x + difx * self.progress, p2.y - dify * self.progress

            return Vec2(pos[0], pos[1])

