import pygame
from pygame.locals import *
from planet import *
from trade import *
from rocket import *
from gui import *

pygame.init()
screen = pygame.display.set_mode((1280, 700))
clock = pygame.time.Clock()

planets = [Planet(640, 350, 0), Planet(800, 200, 0)]
rockets = [Rocket(planets[0])]
routes = [Traderoute([planets[1], planets[0]])]

rockets[0].route = routes[0]

guiElements = []
guiElements.append(Button(Vec2(0, 0), Vec2(10, 10), ("planet.png", "testClick.png", "testHover.png")))


mousePos = (0, 0)
mouseVec = Vec2(0,0)
mouseClicks = (False, False, False)

framerate = 50
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    mousePos = pygame.mouse.get_pos()
    mouseVec = Vec2(mousePos)

    mouseClicks = pygame.mouse.get_pressed()

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

    for element in guiElements:
        element.update(mouseVec, mouseClicks)
        element.draw(screen)

    pygame.display.flip()
    clock.tick(framerate)

