import pygame

from Vec2 import *

BUTTON_DEFAULT = 0
BUTTON_HOVER = 1
BUTTON_CLICK_START = 2
BUTTON_CLICK = 3

class GUIElement:
    parentPos = Vec2(0, 0)
    pos = Vec2(0, 0)

    def __init__(self, parentPos, pos):
        self.parentPos = parentPos
        self.pos = pos
        
    def getPos(self):
        return self.pos

    def setParent(self, parent):
        self.paretPos = parent

    def setPos(self, pos):
        self.pos = pos

    def draw(self, screen):
        pass
    
    #Mouse pos is Vec2, mouseClicks is a tupple of mouse button states
    def update(self, mousePos, mouseClicks):
        pass
        

class Button(GUIElement):
    state = 0
    images = []
    size = Vec2(0, 0)

    onClick = None

    def __init__(self, parentPos, pos, imageNames):
        super(GUIElement, self).__init__()
        
        #loading images
        for i in imageNames:
            image = pygame.image.load(i)
            self.size = Vec2(image.get_size())

            self.images.append(image)

    def update(self, mousePos, mouseClicks):
        super().update(mousePos, mouseClicks)

        #Calculating the edges of the button
        bottomRight = self.pos + self.size

        if(mousePos >= self.pos and mousePos <= bottomRight):
            if(mouseClicks[0] == 1):
                self.state = BUTTON_CLICK_START
            else:
                #The button was released this frame, run onClick
                if(self.state == BUTTON_CLICK_START):
                    if(self.onClick != None):
                        self.onClick()
                
                self.state = BUTTON_HOVER
        else:
            self.state = BUTTON_DEFAULT

    
    def draw(self, screen):
        super().draw(screen)
        
        currentImage = self.images[0]
        if(self.state == BUTTON_CLICK_START):
            currentImage = self.images[1]
        if(self.state == BUTTON_HOVER):
            currentImage = self.images[2]

        screen.blit(currentImage, (self.pos.x, self.pos.y))
    
    def setOnClick(self, func):
        self.onClick = func

def Window(GUIElement):
    background = None
    size = Vec2(0, 0)

    children = []

    def __init__(self, parentPos, pos, backgroundName):
        super(GUIElement, self).__init__()

        self.background = pygame.image.load(backgroundName)

    def addChild(child):
        pass
