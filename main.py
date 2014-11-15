import pygame, random
from pygame.locals import *
from planet import *
from trade import *
from rocket import *
from gui import *
from Vec2 import *
from renderer import *

pygame.init()
clock = pygame.time.Clock()

planets = [Planet(Vec2(0, 0), 0)]
rockets = [Rocket(planets[0])]
routes = []

guiElements = []
#guiElements.append(Button(Vec2(0, 0), Vec2(10, 10), ("planet.png", "testClick.png", "testHover.png")))
guiElements.append(Window(Vec2(0, 0), Vec2(100, 100), "testWindow.png"))
guiElements[0].addChild(Button(Vec2(100, 300), Vec2(10, 10), ("planet.png", "testClick.png", "testHover.png")))
guiElements[0].addChild(Button(Vec2(100, 300), Vec2(100, 10), ("planet.png", "testClick.png", "testHover.png")))
guiElements[0].addChild(GUIImage(Vec2(100, 300), Vec2(150, 10), "testHover.png"))



# Generate planets
for x in range(-10, 10):
    for y in range(-10, 10):
        if (x != 0 or y != 0) and random.randint(0, 3) > 0:
            offset = Vec2(random.randint(-90, 90), random.randint(-90, 90))
            planet = Planet(Vec2(x, y) * 300 + offset, 0)
            planets.append(planet)

            if abs(x) == 1 and abs(y) == 1: # Create a trade route to a planet close to earth
                routes.append(Traderoute((planets[0], planet)))

rockets[0].route = routes[0]

mousePos = (0, 0)
mouseVec = Vec2(0,0)
mouseClicks = (False, False, False)

background = pygame.image.load("Background.png")
glow = pygame.image.load("selection.png")
framerate = 50
running = True
yscroll = 0
xscroll = 0
renderer = Renderer()
cameraSpeed = 800 # in pixels per second
dt = 1 / framerate
selection = planets[0]
while running:
    renderer.clear()
    renderer.draw(background, Vec2(0,0), True)
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
            elif event.key == K_SPACE:
                renderer.camera = Vec2(0,0)
        if event.type == KEYUP:
            if event.key == K_w:
                yscroll += 1
            elif event.key == K_s:
                yscroll -= 1
            elif event.key == K_a:
                xscroll += 1
            elif event.key == K_d:
                xscroll -= 1

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            for planet in planets:
                if planet.wasClicked(mousePos):
                    selection = planet

    # Update objects
    for rocket in rockets:
        rocket.update(dt)

    renderer.move_camera(Vec2(xscroll, yscroll) * dt * cameraSpeed)

    # Draw shit
    for traderoute in routes:
        traderoute.draw(renderer)

    if selection != None:
        renderer.draw(glow, selection.get_coords())

    for planet in planets:
        planet.draw(renderer)

    for rocket in rockets:
        rocket.draw(renderer)

    for element in guiElements:
        element.update(mouseVec, mouseClicks)
        element.draw(renderer)

    pygame.display.flip()
    dt = clock.tick(framerate) / 1000

