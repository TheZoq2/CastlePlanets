import pygame
from pygame.locals import *
from planet import *
from trade import *
from rocket import *
from gui import *
from Vec2 import *
from renderer import *

pygame.init()
clock = pygame.time.Clock()

planets = [Planet(0, 0, 0), Planet(100, -200, 0)]
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
yscroll = 0
xscroll = 0
renderer = Renderer()
cameraSpeed = 400 # in pixels per second
while running:
    dt = 1 / framerate
    
    renderer.clear()
    mousePos = pygame.mouse.get_pos()
    mouseVec = Vec2(mousePos)

    mouseClicks = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

        if event.type == KEYDOWN:
            if event.key == K_w:
                yscroll -= 1
            elif event.key == K_s:
                yscroll += 1
            elif event.key == K_a:
                xscroll -= 1
            elif event.key == K_d:
                xscroll += 1
        if event.type == KEYUP:
            if event.key == K_w:
                yscroll += 1
            elif event.key == K_s:
                yscroll -= 1
            elif event.key == K_a:
                xscroll += 1
            elif event.key == K_d:
                xscroll -= 1

    # Update objects
    for rocket in rockets:
        rocket.update(dt)

    renderer.move_camera(Vec2(xscroll, yscroll) * dt * cameraSpeed)

    # Draw shit
    for planet in planets:
        renderer.draw(planet)

    for traderoute in routes:
        pass

    for rocket in rockets:
        renderer.draw(rocket)

    for element in guiElements:
        element.update(mouseVec, mouseClicks)
        element.draw(screen)

    pygame.display.flip()
    clock.tick(framerate)

