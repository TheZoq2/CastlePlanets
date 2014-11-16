import pygame, random, math
from Vec2 import *

FOOD_CONSUMPTION = 10
PRODUCTION_PER_PERSON = 0.1
POPULATION_GROWTH_PER_FOOD = 40

PlanetImgs = []
for i in range(5):
    PlanetImgs += [pygame.image.load("Planets/planet" + str(i+1) + ".png")]
PlanetImgs += [pygame.image.load("Planets/Earth.png")]

print(PlanetImgs)

# Nothing should be changed
types = ["Food", "Wood", "Iron", "Nothing", "Nothing2", "Earth"]
resourceNames = ["Food", "Wood", "Iron"]

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
        self.popFloat = population #Float value to allow pop to grow every other frame
        self.ownage = ownage
            

        if self.name == None:
            self.name = random.choice(names)
        if self.type == None:
            self.type = self.generate_type(types)
        if self.size == None:
            self.size = random.uniform(0.1, 0.7)
        if self.ownage == None:
            self.ownage = False

        self.resources = {
                "Food": 0,
                "Wood": 0,
                "Iron": 0
            }
        self.maxResources = {
                "Food": 1000,
                "Wood": 1000,
                "Iron": 1000
            }
        self.production = {
                "Food": 3,
                "Wood": 3,
                "Iron": 3
            }

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

    def getMaxResources(self, res):
        return maxResources(res)

    def draw(self, renderer):
        renderer.draw(self.img, self.pos)

    def generate_type(self, types):
        return types[random.randint(0, 2)]

    def population_growth(self):
        if self.population <= self.resources["Food"]:
            self.resources["Food"] -= self.population / FOOD_CONSUMPTION
            self.popFloat += self.popFloat / POPULATION_GROWTH_PER_FOOD
            self.population = math.floor(self.popFloat)
        else:
            self.population = self.resources["Food"]
            self.resources["Food"] = 0
    
    def getResourceProduction(self, resource):
        return math.floor(self.production[resource] * PRODUCTION_PER_PERSON * self.population)

    def produce(self):
        for type in resourceNames:
            cProd = self.getResourceProduction(type)

            self.resources[type] = self.resources[type] + cProd

    def update(self, dt):
        """if self.timer >= 100:
            self.timer = 0
            # planet producing food will eat all of it, eat less or produce more!
            self.population_growth()
            if self.all_resources() + self.population >= int(self.size * 10000):
                self.resources[self.type] = int(self.size * 10000) - self.all_resources()
            else:
                self.resources[self.type] += self.population
        else:
            self.timer += 1"""

        self.timer += dt

        if(self.timer >= 1):
            self.timer = self.timer - 1
            
            self.population_growth()
            self.produce()

    def add_resources(self, type, amount):
        if self.resources[Type] + amount < self.maxResources[type]:
            self.resources[type] += amount
            return amount
        else:
            res = self.maxResources - self.resources[type]
            self.resources[type] = self.maxResources[type]
            return res


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
