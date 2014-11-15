import pygame, random
from Vec2 import *

PlanetImgs = []
for i in range(5):
    PlanetImgs += [pygame.image.load("Planets/planet" + str(i+1) + ".png")]
PlanetImgs += [pygame.image.load("Planets/Earth.png")]

print(PlanetImgs)

# Nothing should be changed
types = ["Food", "Wood", "Iron", "Nothing", "Nothing2", "Earth"]
with open('planetnames.txt', 'r') as n:
    names = []
    for line in n:
        names.append(line)

class Planet:
    def __init__(self, name, pos, type, size, resources, population):
        self.name = name
        self.pos = pos
        self.type = type
        self.size = size
        self.resources = resources
        self.population = population
        if self.name == None:
            self.name = random.choice(names)
        if self.type == None:
            self.type = self.generate_type(types)
        if self.size == None:
            self.size = random.uniform(0.1, 0.7)
        if self.resources == None:
            self.resources = {}
            for type in types:
                self.resources[type] = 0
            self.resources = {str(self.type): 100 * random.randint(1,5)}

    def get_coords(self):
        return self.pos

    def all_resources(self):
        res = 0
        for type in types:
            res += self.resources[type]
        return res

    def draw(self, renderer):
        img = PlanetImgs[types.index(self.type)]
        renderer.draw(pygame.transform.scale(img, (int(img.get_width() * self.size), int(img.get_height() * self.size))), self.pos)

    def generate_type(self, types):
        return types[random.randint(0, 2)]

    def update(self):
        if self.all_resources() + self.population >= self.size * 10000:
            self.resources[self.type] = self.size * 10000 - self.all_resources()
        else:
            self.resources[self.type] += self.population

    def add_resources(self, type, amount):
        res = 0
        for type in types:
            res += self.resources[type]
            
        if self.size * 10000 - self.all_resources() < amount:
            self.resources[type] += amount - self.size * 10000 + self.all_resources()
            return amount - self.size * 10000 + self.all_resources()
        else:
            self.resources[type] += amount
            return amount

    def get_resources(self, type, amount):
        if self.resources[type] >= amount:
            self.resources[type] -= amount
            return amount
        else:
            res = self.resources[type]
            self.resources[type] = 0
            return res
