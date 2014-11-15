import pygame
import pdb

from Vec2 import *

BUTTON_DEFAULT = 0
BUTTON_HOVER = 1
BUTTON_CLICK_START = 2
BUTTON_CLICK = 3

class GUIElement:
    parentPos = Vec2(0, 0)
    pos = Vec2(0, 0)
    truePos = Vec2(0, 0)

    def __init__(self, parentPos, pos):
        self.parentPos = parentPos
        self.pos = pos

        
    def getPos(self):
        return self.pos

    def setParentPos(self, parent):
        self.parentPos = parent
        self.calcTruePos()

    def setPos(self, pos):
        self.pos = pos
        calcTruePos()

    def draw(self, renderer):
        pass
    
    #Mouse pos is Vec2, mouseClicks is a tupple of mouse button states
    def update(self, mousePos, mouseClicks):
        self.calcTruePos()

    def calcTruePos(self):
        self.truePos = self.pos + self.parentPos

class Button(GUIElement):
    state = 0
    images = []
    size = Vec2(0, 0)

    onClick = None

    def __init__(self, parentPos, pos, imageNames):
        super().__init__(parentPos, pos)
        #loading images
        for i in imageNames:
            image = pygame.image.load(i)
            self.size = Vec2(image.get_size())

            self.images.append(image)

    def update(self, mousePos, mouseClicks):
        super().update(mousePos, mouseClicks)

        #Calculating the edges of the button
        bottomRight = self.truePos + self.size

        if(mousePos >= self.truePos and mousePos <= bottomRight):
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

    
    def draw(self, renderer):
        super().draw(renderer)
        
        currentImage = self.images[0]
        if(self.state == BUTTON_CLICK_START):
            currentImage = self.images[1]
        if(self.state == BUTTON_HOVER):
            currentImage = self.images[2]

        renderer.draw(currentImage, self.truePos, True)
    
    def setOnClick(self, func):
        self.onClick = func

class Window(GUIElement):
    background = None
    size = Vec2(0, 0)

    children = []

    def __init__(self, parentPos, pos, backgroundName):
        super().__init__(parentPos, pos)

        self.background = pygame.image.load(backgroundName)

    def update(self, mousePos, mouseClicks):
        super().update(mousePos, mouseClicks)

        #uppdating all children
        for child in self.children:
            child.setParentPos(self.truePos)
            child.update(mousePos, mouseClicks)

    def draw(self, renderer):
        super().draw(renderer)

        renderer.draw(self.background, self.truePos, True)
        
        #Draw all the children
        for child in self.children:
            child.draw(renderer)


    def addChild(self, child):
        child.setParentPos(self.truePos)
        self.children.append(child)
