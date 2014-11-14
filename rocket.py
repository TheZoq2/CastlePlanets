import pygame

rocketImg = pygame.image.load("rocket.png")

class Rocket:
    def __init__(self, planet):
        self.planet = planet

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(rocketImg, (self.planet.x, self.planet.y))

