import pygame

planetImgs = [pygame.image.load("planet.png")]

class Planet:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type



    def draw(self, screen):
        screen.blit(planetImgs[self.type], (self.x, self.y))

    def get_coords(self):
        return (self.x, self.y)
