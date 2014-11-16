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
    def __init__(self, name, pos, type, size, population, ownage):
        self.name = name
        self.pos = pos
        self.type = type
        self.size = size
        self.population = population
        self.ownage = ownage
        if self.name == None:
            self.name = random.choice(names)
        if self.type == None:
            self.type = self.generate_type(types)
        if self.size == None:
            self.size = random.uniform(0.1, 0.7)
        if self.ownage == None:
            self.ownage = False

        self.resources = {}
        for type in types:
            self.resources[type] = 0

        if self.name == "Earth":
            self.resources['Food'] = 100

        img = PlanetImgs[types.index(self.type)]
        self.img = pygame.transform.scale(img, (int(img.get_width() * self.size), int(img.get_height() * self.size)))

        self.timer = 0

    def get_coords(self):
        return self.pos

    def all_resources(self):
        res = 0
        for type in types:
            res += self.resources[type]
        return res

    def draw(self, renderer):
        renderer.draw(self.img, self.pos)

    def generate_type(self, types):
        return types[random.randint(0, 2)]

    def population_growth(self):
        if self.population <= self.resources["Food"]:
            self.resources["Food"] -= self.population
            self.population += self.population // 10
        else:
            self.population = self.resources["Food"]
            self.resources["Food"] = 0


    def update(self, dt):
        if self.timer >= 100:
            self.timer = 0
            # planet producing food will eat all of it, eat less or produce more!
            self.population_growth()
            if self.all_resources() + self.population >= int(self.size * 10000):
                self.resources[self.type] = int(self.size * 10000) - self.all_resources()
            else:
                self.resources[self.type] += self.population
        else:
            self.timer += 1

    def add_resources(self, type, amount):
        self.resources[type] += amount


    def get_resources(self, type, amount):
        if self.resources[type] >= amount:
            self.resources[type] -= amount
            return amount
        else:
            res = self.resources[type]
            self.resources[type] = 0
            return res

    def claim(self):
        self.ownage = True
