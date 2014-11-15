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

        self.cargo_type = None
        self.cargo_max = 10
        self.cargo_current = 0

    def load_cargo(target_planet):
        target_planet.get_resources(self.cargo_type, self.cargo_max)

    def unload_cargo(target_planet):
        target_planet.add_resources(self.cargo_type, self.cargo_current)

    def update(self, dt):
        if self.route:
            diff = self.target.get_coords() - self.pos

            if diff.getLen() <= 40:
                if self.target == self.route.path[0]:
                    unload_cargo(self.target)
                    load_cargo(self.target)
                    self.target = self.route.path[1]
                else:
                    unload_cargo(self.target)
                    load_cargo(self.target)
                    self.target = self.route.path[0]
            else:
                self.pos += diff.normalized() * self.speed * dt

    def draw(self, renderer):
        renderer.draw(rocketImg, self.pos)
