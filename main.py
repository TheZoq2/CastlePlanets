import pygame
from pygame.locals import *
from planet import *
from trade import *
from rocket import *

pygame.init()
screen = pygame.display.set_mode((1280, 700))
clock = pygame.time.Clock()

planets = [Planet(640, 350, 0)]
rockets = [Rocket(planets[0])]
routes = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    for planet in planets:
        planet.draw(screen)

    for traderoute in routes:
        pass

    for rocket in rockets:
        rocket.draw(screen)

    pygame.display.flip()

