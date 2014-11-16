import pygame
from Vec2 import *

def routable_planets(source_planet, planets):
    close_planets = []
    for planet in planets:
        if planet != source_planet and getDistance(source_planet.get_coords(), planet.get_coords()) < 500:
            close_planets.append(planet)
    return close_planets

class Traderoute:
    def __init__(self, path, cargo):
        self.path = path
        self.cargo = cargo
        self.color = (255,255,255)
        #print(path, len(path), len(path) - 1)

    def draw(self, renderer):
        for i in range(len(self.path) - 1):
            p1 = self.path[i].get_coords()
            p2 = self.path[i+1].get_coords()
            diff = p2 - p1
            seg_start = 0
            while seg_start < diff.getLen():
                renderer.line(p1 + diff.normalized() * seg_start, p1 + diff.normalized() * (seg_start + 15))
                seg_start += 25

    
    def getLowestDistance(self, pos):
        pass

