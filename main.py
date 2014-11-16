import pygame, random
from pygame.locals import *
from planet import *
from trade import *
from rocket import *
from gui import *
from Vec2 import *
from renderer import *
from Text import *
import pdb

pygame.init()
clock = pygame.time.Clock()

routes = []

guiElements = []
#guiElements.append(Button(Vec2(0, 0), Vec2(10, 10), ("planet.png", "testClick.png", "testHover.png")))
guiElements.append(Window(Vec2(0, 0), Vec2(0, 500), "testWindow.png"))
#guiElements.append(testWindow)
guiElements.append(Window(Vec2(0, 0), Vec2(980, 0), "testWindow2.png"))

add_traderoute = Button(Vec2(100, 300), Vec2(200, 10), ("planet.png", "testClick.png", "testHover.png"))
guiElements[0].addChild(add_traderoute)

planet_name = TextObject(Vec2(100,200), Vec2(10, 10), Vec2(100, 20), "Planet")
planet_population = TextObject(Vec2(100, 200), Vec2(100, 75), Vec2(200, 200), "P: -")
planet_food = TextObject(Vec2(100, 200), Vec2(100, 100), Vec2(200, 200), "~FOOD~ -")
planet_wood = TextObject(Vec2(100, 200), Vec2(100, 125), Vec2(200, 200), "~WOOD~ -")
planet_iron = TextObject(Vec2(100, 200), Vec2(100, 150), Vec2(200, 200), "~IRON~ -")

guiElements[0].addChild(planet_name)
guiElements[0].addChild(planet_population)
guiElements[0].addChild(planet_food)
guiElements[0].addChild(planet_wood)
guiElements[0].addChild(planet_iron)

guiElements[1].addChild(Button(Vec2(100, 300), Vec2(100, 10), ("planet.png", "testClick.png", "testHover.png")))
#guiElements[0].addChild(GUIImage(Vec2(100, 300), Vec2(150, 10), "testHover.png"))
#guiElements[0].addChild(GUIImage(Vec2(200, 100), Vec2(200, 10), "Hello world"))
#guiElements[1].addChild(TextWord(Vec2(100, 100), Vec2(200, 10), "Hello world"))
textObject = TextObject(Vec2(100, 100), Vec2(10, 10), Vec2(280, 960), "If this is an image, it works: ~FOOD~. You can only have a ciration amount of wood, which is represented by ~WOOD_MAX~, ~IRON_MAX~")
guiElements[1].addChild(textObject)

textObject.setText("This text has been updated with the ^red^power of ~FOOD~")


planets = [Planet("Earth", Vec2(0, 0), "Earth", 0.5, 30, True)]
planets[0].add_resources("Food", 300)
#rockets = [Rocket(planets[0])]
rockets = []

# Generate planets
for x in range(-10, 10):
    for y in range(-10, 10):
        if (x != 0 or y != 0) and random.randint(0, 3) > 0:
            offset = Vec2(random.randint(-90, 90), random.randint(-90, 90))
            planet = Planet(None, Vec2(x, y) * 300 + offset, None, None, 0, None)
            planets.append(planet)

            #if abs(x) == 1 and abs(y) == 1: # Create a trade route to a planet close to earth
            #    routes.append(Traderoute((planets[0], planet), ('Food', 'Iron')))

#rockets[0].route = routes[0]

mousePos = (0, 0)
mouseVec = Vec2(0,0)
mouseClicks = (False, False, False)

background = pygame.image.load("bg_small.png")
glow = pygame.image.load("selection.png")
multiglow = pygame.image.load("multiselect.png")
framerate = 50
running = True
yscroll = 0
xscroll = 0
renderer = Renderer()
cameraSpeed = 800 # in pixels per second

dt = 1 / framerate
#selection = planets[0]
selection = None

multiselect = []

def addTradeRoute():
    if selection != None:
        #multiselect = []
        for planet in routable_planets(selection, planets):
            #print(planet.name)
            multiselect.append(planet)

add_traderoute.setOnClick(addTradeRoute)

def clickedPlanet(mouseVec):
    for planet in planets:
        planet_screen_pos = planet.get_coords() - renderer.camera
        planet_screen_pos += Vec2((SCREEN_WIDTH - 300) / 2, (SCREEN_HEIGHT - 200) / 2)
        diff = mouseVec - planet_screen_pos
        if diff.getLen() <= 128 * planet.size:
            return planet
    return None

def update_dashboard(selection):
    planet_name.setText(selection.name)
    planet_population.setText("P: %i" % selection.population)
    planet_food.setText("~FOOD~ %i" % selection.resources['Food'])
    planet_wood.setText("~WOOD~ %i" % selection.resources['Wood'])
    planet_iron.setText("~IRON~ %i" % selection.resources['Iron'])


dragging = False
while running:
    renderer.clear()
    renderer.draw(background, Vec2(0,0), True)
    mousePos = pygame.mouse.get_pos()
    mouseVec = Vec2(mousePos)
    mouseRel = Vec2(pygame.mouse.get_rel())
    if dragging:
        renderer.move_camera(mouseRel * -1)

    mouseClicks = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:# or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

        if event.type == KEYDOWN:
            if event.key == K_w:
                yscroll = -1
            elif event.key == K_s:
                yscroll = 1
            elif event.key == K_a:
                xscroll = -1
            elif event.key == K_d:
                xscroll = 1
            elif event.key == K_SPACE:
                renderer.camera = Vec2(0, 0)
        if event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                yscroll = 0
            elif event.key == K_a or event.key == K_d:
                xscroll = 0

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            planet = clickedPlanet(mouseVec)
            if planet in multiselect:
                print('Multiselected %s -> %s' % (selection.name, planet.name))
                new_route = Traderoute((selection, planet), ('Food', 'Iron'))
                routes.append(new_route)
                rocket = Rocket(selection)
                rockets.append(rocket)
                rocket.route= new_route
                multiselect = []
            elif planet != None:
                if planet in [x.path[0] for x in routes] + [x.path[1] for x in routes] or planet == planets[0]:
                    selection = planet
                    scale = Vec2(256, 256) * selection.size
                    glow_scaled = pygame.transform.scale(glow, (int(scale.x) + 30, int(scale.y) + 30))
            else:
                dragging = True
                multiselect = []

        if event.type == MOUSEBUTTONUP and event.button == 1:
            dragging = False

    renderer.move_camera(Vec2(xscroll, yscroll) * dt * cameraSpeed)
    if multiselect != []:
        for planet in multiselect:
            if ((selection, planet) in [(x.path[1], x.path[0]) for x in routes]) or ((selection, planet) in [(x.path[0], x.path[1]) for x in routes]):
                multiselect.remove(planet)
            else:
                scale = Vec2(256, 256) * planet.size
                multi_glow_scaled = pygame.transform.scale(multiglow, (int(scale.x) + 30, int(scale.y) + 30))
                renderer.draw(multi_glow_scaled, planet.get_coords())

    # Update objects
    for rocket in rockets:
        rocket.update(dt)

    for planet in planets:
        planet.update(dt)

    if selection != None:
        update_dashboard(selection)

    # Draw shit
    for traderoute in routes:
        traderoute.draw(renderer)

    if selection != None:
        renderer.draw(glow_scaled, selection.get_coords())

    for planet in planets:
        planet.draw(renderer)

    for rocket in rockets:
        rocket.draw(renderer)

    for element in guiElements:
        element.update(mouseVec, mouseClicks)
        element.draw(renderer)

    pygame.display.flip()
    dt = clock.tick(framerate) / 1000
