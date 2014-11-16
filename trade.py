import pygame
from Vec2 import *

TRADE_ICON = pygame.transform.scale(pygame.image.load("TradeIcon.png"), (32, 32))


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
        self.isSelected = False
        #print(path, len(path), len(path) - 1)


        #Calculatnig center pos
        dist = path[1].get_coords() - path[0].get_coords()
        self.center = path[0].get_coords() + dist / 2

    def draw(self, renderer):
        for i in range(len(self.path) - 1):
            p1 = self.path[i].get_coords()
            p2 = self.path[i+1].get_coords()
            diff = p2 - p1
            seg_start = 0
            
            renderer.draw(TRADE_ICON, self.center)

            while seg_start < diff.getLen():
                color = (255,255,255)
                if self.isSelected == True:
                    color = (150, 150, 255)

                renderer.line(p1 + diff.normalized() * seg_start, p1 + diff.normalized() * (seg_start + 15), color=color)
                seg_start += 25
    
    def setSelected(self, selected):
        self.isSelected = selected
    
    def getCenter(self):
        return self.center
