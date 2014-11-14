import pygame
from pygame.locals import *
from planet import *
from trade import *
from rocket import *

pygame.init()
screen = pygame.display.set_mode((1280, 700))
clock = pygame.time.Clock()

planets = [Planet(640, 350, 0), Planet(800, 200, 0)]
rockets = [Rocket(planets[0])]
routes = [Traderoute([planets[1], planets[0]])]

rockets[0].route = routes[0]

framerate = 50
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    # Update objects
    for rocket in rockets:
        rocket.update(1 / framerate)

    # Draw shit
    for planet in planets:
        planet.draw(screen)

    for traderoute in routes:
        pass

    for rocket in rockets:
        rocket.draw(screen)

    pygame.display.flip()
    clock.tick(framerate)

