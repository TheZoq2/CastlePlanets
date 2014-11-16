import pygame, math
from Vec2 import *


rocketImg = pygame.image.load("rocket.png")

ROCKET_SPEED = 100

class Rocket:
    def __init__(self, planet):
        self.planet = planet
        self.route = None
        self.speed = ROCKET_SPEED
        self.pos = planet.get_coords()
        self.target = planet

        self.cargo_type = None
        self.cargo_max = 10
        self.cargo_current = 0

    def load_cargo(self, target_planet, cargo):
        self.cargo_current = target_planet.get_resources(cargo, self.cargo_max)
        self.cargo_type = cargo

    def unload_cargo(self, target_planet):
        if self.cargo_type != None:
            target_planet.add_resources(self.cargo_type, self.cargo_current)

    def update(self, dt):
        if self.route:
            diff = self.target.get_coords() - self.pos

            if diff.getLen() <= 40:
                if self.target == self.route.path[0]:
                    self.unload_cargo(self.target)
                    self.load_cargo(self.target, self.route.cargo[0])
                    self.target = self.route.path[1]
                else:
                    self.unload_cargo(self.target)
                    self.load_cargo(self.target, self.route.cargo[1])
                    self.target = self.route.path[0]
            else:
                self.pos += diff.normalized() * self.speed * dt

    def draw(self, renderer):
        if self.route:
            dir = self.target.get_coords() - self.pos
            angle = math.degrees(Vec2(dir.y, dir.x).getAngle()) + 180
            renderer.draw(pygame.transform.rotate(rocketImg, angle), self.pos)
        else:
            renderer.draw(rocketImg, self.pos)
