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
guiElements.append(Window(Vec2(0, 0), Vec2(0, 500), "GUI/bottombar.png"))
#guiElements.append(testWindow)
guiElements.append(Window(Vec2(0, 0), Vec2(980, 0), "GUI/sidebar.png"))
guiElements.append(Window(Vec2(0, 0), Vec2(0, 0), "GUI/topbar.png"))

add_traderoute = Button(Vec2(100, 300), Vec2(200, 30), ("trade_route_button.png", "trade_route_button.png", "trade_route_button.png"))
add_rocket = Button(Vec2(0,0), Vec2(890, 30), ("rocket.png", "rocket.png", "rocket.png"))
guiElements[0].addChild(add_traderoute)
guiElements[0].addChild(add_rocket)

planet_name = TextObject(Vec2(100,200), Vec2(100, 30), Vec2(100, 20), "Planet")
planet_population = TextObject(Vec2(100, 200), Vec2(100, 75), Vec2(200, 200), "~POP~ -")
planet_food = TextObject(Vec2(100, 200), Vec2(100, 100), Vec2(200, 200), "~FOOD~ -")
planet_wood = TextObject(Vec2(100, 200), Vec2(100, 125), Vec2(200, 200), "~WOOD~ -")
planet_iron = TextObject(Vec2(100, 200), Vec2(100, 150), Vec2(200, 200), "~IRON~ -")

guiElements[0].addChild(planet_name)
guiElements[0].addChild(planet_population)
guiElements[0].addChild(planet_food)
guiElements[0].addChild(planet_wood)
guiElements[0].addChild(planet_iron)

planetWindow = guiElements[0]
tradeWindow = Window(Vec2(0,0), Vec2(10000,500), "GUI/bottombar.png") 
guiElements.append(tradeWindow)

tradePlanetNames = [
            TextObject(Vec2(100,200), Vec2(100, 30), Vec2(200, 200), "Planet"),
            TextObject(Vec2(100,200), Vec2(500, 30), Vec2(200, 200), "Planet")
        ]

tradeTransferText = [
            TextObject(Vec2(100, 200), Vec2(300, 40), Vec2(200, 200), "Transfering"),
            TextObject(Vec2(100, 200), Vec2(300, 60), Vec2(200, 200), "Transfering")
        ]

tradeResourceButtons = [
        Button(Vec2(0, 0), Vec2(100, 50), ("Resources/food.png", "Resources/food.png", "Resources/food.png")),
        Button(Vec2(0, 0), Vec2(100, 80), ("Resources/wood.png", "Resources/wood.png", "Resources/wood.png")),
        Button(Vec2(0, 0), Vec2(100, 100), ("Resources/iron.png", "Resources/iron.png", "Resources/iron.png")),

        Button(Vec2(0, 0), Vec2(500, 50), ("Resources/food.png", "Resources/food.png", "Resources/food.png")),
        Button(Vec2(0, 0), Vec2(500, 80), ("Resources/wood.png", "Resources/wood.png", "Resources/wood.png")),
        Button(Vec2(0, 0), Vec2(500, 100), ("Resources/iron.png", "Resources/iron.png", "Resources/iron.png"))
        ]

tradeResourceButtons[0].setOnClick(lambda: setShipCargo(0, "Food"))
tradeResourceButtons[1].setOnClick(lambda: setShipCargo(0, "Wood"))
tradeResourceButtons[2].setOnClick(lambda: setShipCargo(0, "Iron"))
tradeResourceButtons[3].setOnClick(lambda: setShipCargo(1, "Food"))
tradeResourceButtons[4].setOnClick(lambda: setShipCargo(1, "Wood"))
tradeResourceButtons[5].setOnClick(lambda: setShipCargo(1, "Iron"))

for i in tradeTransferText:
    tradeWindow.addChild(i)

for i in tradePlanetNames:
    tradeWindow.addChild(i)

for i in tradeResourceButtons:
    tradeWindow.addChild(i)

RESOURCE_TO_IMAGE = {
            "Food": "~FOOD~",
            "Wood": "~WOOD~",
            "Iron": "~IRON~"
        }

#guiElements[1].addChild(Button(Vec2(100, 300), Vec2(100, 10), ("planet.png", "testClick.png", "testHover.png")))
#guiElements[0].addChild(GUIImage(Vec2(100, 300), Vec2(150, 10), "testHover.png"))
#guiElements[0].addChild(GUIImage(Vec2(200, 100), Vec2(200, 10), "Hello world"))
#guiElements[1].addChild(TextWord(Vec2(100, 100), Vec2(200, 10), "Hello world"))


resourceText = TextObject(Vec2(0,0), Vec2(10,5), Vec2(1000, 1000), "")
guiElements[2].addChild(resourceText)

logText = TextObject(Vec2(100, 100), Vec2(30, 50), Vec2(250, 960), "Game Log")
guiElements[1].addChild(logText)

planets = [Planet("Earth", Vec2(0, 0), "Earth", 0.5, 30, True)]
selection = planets[0]
planets[0].add_resources("Food", 1000)
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

def gameLog(str):
    logText.setText(str + ' /n /n ' + logText.getText())

def addTradeRoute():
    if selection != None:
        #multiselect = []
        for planet in routable_planets(selection, planets):
            #print(planet.name)
            multiselect.append(planet)

def addRocket():
    if selection != None and isinstance(selection, Traderoute):
        rocket = Rocket(selection.path[0])
        rocket.route = selection
        rockets.append(rocket)

def setShipCargo(ID, cargo):
    if(isinstance(selection, Traderoute)):
        tempCargo = selection.cargo
        
        newCargo = None
        if(ID == 0):
            newCargo = (cargo, tempCargo[1])
        if(ID == 1):
            newCargo = (tempCargo[0], cargo)
        selection.cargo = newCargo
        #selection.cargo[ID] = cargo[ID]


def getTradeCargo(ID):
    if(isinstance(selection, Traderoute)):
        return selection.cargo[ID]


add_traderoute.setOnClick(addTradeRoute)
add_rocket.setOnClick(addRocket)

def payToWin(source_planet, target_planet, type, cost, population, food):
    print('payToWin')
    print(source_planet.population)
    print(source_planet.resources[type])
    if source_planet.population >= population and source_planet.resources[type] >= cost and source_planet.resources['Food'] >= food:
        print('transaction approved')
        source_planet.resources[type] -= cost
        if not target_planet.ownage:
            print('undiscovered ground!')
            source_planet.population -= population
            # source_planet.popFloat -= population
            target_planet.population = population
            # target_planet.popFloat = population

            source_planet.resources['Food'] -= food
            target_planet.resources['Food'] += food
        target_planet.ownage = True
        gameLog('New traderoute established between %s and %s' % (source_planet.name, target_planet.name))
        return True
    else:
        gameLog('Missing resources')
        return False


def clickedPlanet(mouseVec):
    for planet in planets:
        planet_screen_pos = planet.get_coords() - renderer.camera
        planet_screen_pos += Vec2((SCREEN_WIDTH - 300) / 2, (SCREEN_HEIGHT - 200) / 2)
        diff = mouseVec - planet_screen_pos
        if diff.getLen() <= 128 * planet.size:
            return planet
    return None

def clickedTradeRoute(mouseVec):
    lowestDist = float("inf")
    lowestRoute = None
    for route in routes:
        #dist = (route.getCenter() - renderer.camera - mouseVec).getLen()
        routeScreenPos = route.getCenter() - renderer.camera
        routeScreenPos += Vec2((SCREEN_WIDTH - 300) / 2, (SCREEN_HEIGHT - 200) / 2)
        dist = mouseVec - routeScreenPos

        if(dist.getLen() < lowestDist):
            lowestRoute = route
            lowestDist = dist.getLen()


    if((lowestDist < 64)):
        return lowestRoute
    return None


def update_dashboard(selection):
    if(isinstance(selection, Planet)):
        tradeWindow.setPos(Vec2(1000, 10500))
        planetWindow.setPos(Vec2(0, 500))

        planet_name.setText(selection.name)
        planet_population.setText("~POP~ %i" % selection.population)
        planet_food.setText("~FOOD~ %i" % selection.resources['Food'])
        planet_wood.setText("~WOOD~ %i" % selection.resources['Wood'])
        planet_iron.setText("~IRON~ %i" % selection.resources['Iron'])
    elif isinstance(selection, Traderoute):
        tradeWindow.setPos(Vec2(0, 500))
        planetWindow.setPos(Vec2(10000, 10000))
        #Getting the info from the path
        resType = selection.cargo

        planets = selection.path
        
        tradePlanetNames[0].setText(planets[0].name)
        tradePlanetNames[1].setText(planets[1].name)
        #abcd
        
        tradeTransferText[0].setText(RESOURCE_TO_IMAGE[selection.cargo[0]] + " >>>>")
        tradeTransferText[1].setText("<<<< " + RESOURCE_TO_IMAGE[selection.cargo[1]])
        

        
        

        

def all_current_resources(planets):
    res = ['Food', 'Wood', 'Iron']
    total_resources = {'Food': 0,
                       'Wood': 0,
                       'Iron': 0,
                       'Population': 0}

    for planet in planets:
        if planet.ownage == True:
            for resource in res:
                total_resources[resource] += planet.resources[resource]
            total_resources['Population'] += planet.population

    return total_resources

def all_max_resources(planets):
    res = ['Food', 'Wood', 'Iron', 'Population']
    max_resources = {'Food': 0,
                     'Wood': 0,
                     'Iron': 0,}

    for planet in planets:
        if planet.ownage == True:
            for resource in res:
                max_resources[resource] += planet.maxResources[resource]

    return max_resources

population_record = 0
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
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_x):
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
            elif event.key == K_ESCAPE:
                multiselect = []
        if event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                yscroll = 0
            elif event.key == K_a or event.key == K_d:
                xscroll = 0

        if event.type == MOUSEBUTTONDOWN:
            clicks = [0,0,0]
            try:
                clicks[event.button - 1] = True
            except Exception:
                print("Scroll is kind of broken")
            for element in guiElements:
                element.update(mouseVec, clicks)
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and mouseVec.x < 980 and mouseVec.y < 500:
            try:
                planet = clickedPlanet(mouseVec)
                route = clickedTradeRoute(mouseVec)

                if planet in multiselect and payToWin(selection, planet, 'Iron', 100, 10, 20):
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
                elif route != None:
                    selection = route
                else:
                    dragging = True
                    multiselect = []
            except Exception:
                print("Hmmmm, something went wrong")


        if event.type == MOUSEBUTTONUP and event.button == 1:
            dragging = False

    resAmnt = all_current_resources(planets)
    resourceText.setText("~FOOD~ %i ~WOOD_MAX~ %i ~IRON_MAX~ %i ~POP~ %i ^green^Population ^green^Record: %i" % (resAmnt['Food'], resAmnt['Wood'], resAmnt['Iron'], resAmnt['Population'], population_record))
    if resAmnt['Population'] == 0:
        gameLog('GAME OVER')
    renderer.move_camera(Vec2(xscroll, yscroll) * dt * cameraSpeed)
    if multiselect != []:
        for planet in multiselect:
            if ((selection, planet) in [(x.path[1], x.path[0]) for x in routes]) or ((selection, planet) in [(x.path[0], x.path[1]) for x in routes]):
                multiselect.remove(planet)
            else:
                scale = Vec2(256, 256) * planet.size
                multi_glow_scaled = pygame.transform.scale(multiglow, (int(scale.x) + 30, int(scale.y) + 30))
                renderer.draw(multi_glow_scaled, planet.get_coords())

    current_resources = all_current_resources(planets)
    current_population = current_resources['Population']
    if current_population > population_record:
        population_record = current_population

    # Update objects
    for rocket in rockets:
        rocket.update(dt)

    for planet in planets:
        planet.update(dt)

    if selection != None:
        update_dashboard(selection)

    # Draw shit
    for traderoute in routes:
        selected = False
        if(traderoute == selection):
            selected = True

        traderoute.draw(renderer, isSelected=selected)

    if selection != None and isinstance(selection, Planet):
        renderer.draw(glow_scaled, selection.get_coords())
    elif selection != None and isinstance(selection, Traderoute):
        pass

    for planet in planets:
        planet.draw(renderer)

    for rocket in rockets:
        rocket.draw(renderer)

    for element in guiElements:
        element.update(mouseVec, mouseClicks)
        element.draw(renderer)


    pygame.display.flip()
    dt = clock.tick(framerate) / 1000
