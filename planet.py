import pygame, random
from Vec2 import *

PlanetImgs = []
for i in range(5):
    PlanetImgs += [pygame.image.load("Planets/planet" + str(i+1) + ".png")]
PlanetImgs += [pygame.image.load("Planets/Earth.png")]

print(PlanetImgs)

types = ["Food", "Wood", "Iron"]
with open('planetnames.txt', 'r') as n:
    names = []
    for line in n:
        names += [line]


class Planet:
    def __init__(self, name, pos, type, size, resources, traderoutes, population):
        self.name = name
        self.pos = pos
        self.type = type
        self.size = size
        self.resources = resources
        self.traderoutes = traderoutes
        self.population = population
        if self.name == None:
            self.name = random.choice(names)
        if self.type == None:
            self.type = self.generate_type(types)
        if self.size == None:
            self.size = random.randint(1, 10) / 10
        if self.resources == None:
            self.resources = {}
            for type in types:
                self.resources[type] = 0
            self.resources = {str(self.type): 100 * random.randint(1,5)}

    def get_coords(self):
        return self.pos

    def draw(self, renderer):
        if self.type == "Earth":
            renderer.draw(PlanetImgs[5], self.pos)
        else:
            renderer.draw(PlanetImgs[types.index(self.type)], self.pos)

    def generate_type(self, types):
        return types[random.randint(0, 2)]

    def update(self):
        pass