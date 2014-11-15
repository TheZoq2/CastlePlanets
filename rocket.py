import pygame, enum
from Vec2 import *

rocketImg = pygame.image.load("rocket.png")

class Rocket:
    def __init__(self, planet):
        self.planet = planet
        self.route = None
        self.speed = 500
        self.pos = planet.get_coords()
        self.target = planet

    def update(self, dt):
        if self.route:
            diff = self.target.get_coords() - self.pos

            if diff.getLen() <= 5:
                if self.target == self.route.path[0]:
                    self.target = self.route.path[1]
                else:
                    self.target = self.route.path[0]
            else:
                self.pos += diff.normalized() * self.speed * dt

    def draw(self, renderer):
        renderer.draw(rocketImg, self.pos)

