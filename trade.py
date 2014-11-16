import pygame
from Vec2 import *

class Traderoute:
    def __init__(self, path, cargo):
        self.path = path
        self.cargo = cargo
        #print(path, len(path), len(path) - 1)

    def draw(self, renderer):
        for i in range(len(self.path) - 1):
            diff = self.path[i+1].get_coords() - self.path[i].get_coords()
            seg_start = 0
            while seg_start < diff.getLen():
                renderer.line(diff.normalized() * seg_start, diff.normalized() * (seg_start + 15))
                seg_start += 25

    def routable_planets(source_planet, planets):
        close_planets = []
        for planet in planets:
            if getDistance(source_planet.get_coords(), planet.get_coords() < 1000):
                close_planets.append(planet)

        return close_planets
