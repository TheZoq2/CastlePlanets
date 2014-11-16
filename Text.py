from gui import *

TEXT_SPECIAL_CHAR = "~"
TEXT_COLOR_CHAR = "^"

FONT_SIZE = 16
TEXT_IMAGE_SIZE = 24
TEXT_LINE_MARGIN = 3

textObjects = {
        "FOOD": pygame.image.load("Resources/food.png"),
        "IRON": pygame.image.load("Resources/iron.png"),
        "IRON_MAX": pygame.image.load("Resources/ironMAX.png"),
        "WOOD": pygame.image.load("Resources/wood.png"),
        "WOOD_MAX": pygame.image.load("Resources/woodMAX.png")
    }

colors = {
        "red": (255, 100, 100),
        "green": (100, 255, 100),
        "blue": (100, 100, 255),
        "yellow": (255, 255, 100)
    }

pygame.font.init()
baseFont = pygame.font.SysFont("arial", FONT_SIZE)

class TextWord(GUIElement):

    def __init__(self, parentPos, pos, text, color=(255,255,255)):
        self.pos = pos
        self.parentPos = parentPos
        self.text = ""
        self.rendered = None
        self.color = color

        super().__init__(parentPos, pos)
        self.text = text

        self.rendered = baseFont.render(text, True, self.color)

    def draw(self, renderer):
        super().draw(renderer)
        renderer.draw(self.rendered, self.truePos, True)

    def update(self, mousePos, mouseClicks):
        super().update(mousePos, mouseClicks)

class TextObject(GUIElement):

    def __init__(self, parentPos, pos, size, text):
        self.text = ""
        self.words = []
        self.size = size
        self.children = []
        self.pos = pos
        self.parentPos = parentPos

        super().__init__(parentPos, pos)

        self.text = text
        
        super().calcTruePos()
        self.generateObjects()


    def update(self, mousePos, mouseClicks):
        super().update(mousePos, mouseClicks)

        #update all children
        for word in self.words:
            word.setParentPos(self.truePos)
            word.update(mousePos, mouseClicks)

    def setText(self, text):
        self.text = text
        self.generateObjects()
    
    def generateObjects(self):
        #Clearing the old words
        self.words = []


        #Split text into words
        rawWords = self.text.split()
        
        cLineStart = TEXT_LINE_MARGIN
        cLineWidth = 0

        for word in rawWords:
            #If this should be replaced by an image
            if(word[0] == TEXT_SPECIAL_CHAR):
                #strip the special char
                newWord = word[1:word.rfind(TEXT_SPECIAL_CHAR)]

                if(newWord in textObjects):
                    imgPath = textObjects[newWord]

                    newLineWidth = cLineWidth + TEXT_IMAGE_SIZE
                    if(newLineWidth > self.size.x):
                        newLineWidth = textSize[0];
                        cLineWidth = 0
                        cLineStart += FONT_SIZE + TEXT_LINE_MARGIN
                        
                        #If the line is full
                        if(cLineStart > self.size.y):
                            break
                        
                    
                    pos = cLineStart - (TEXT_IMAGE_SIZE - FONT_SIZE) / 2
                    newObject = GUIImage(self.truePos, Vec2(cLineWidth, cLineStart), imgPath)
                    
                    newObject.setSize(Vec2(TEXT_IMAGE_SIZE, TEXT_IMAGE_SIZE))

                    cLineWidth = newLineWidth

                    self.addWord(newObject)
                else:
                    print("Special text thingy: ", word, " not recogniced")
            else:
                wordColor = (255,255,255)
                #Checking if the word should have a specific color
                if(word[0] == TEXT_COLOR_CHAR):
                    #Get the color text
                    colorName = word[1:word.rfind(TEXT_COLOR_CHAR)]

                    print(colorName)

                    if(colorName in colors):
                        wordColor = colors[colorName]
                    
                    word = word[word.rfind(TEXT_COLOR_CHAR) + 1:]

                    

                #calculating the size of the text
                textSize = baseFont.size(word + " ")

                newLineWidth = cLineWidth + textSize[0]
                if(newLineWidth > self.size.x):
                    newLineWidth = textSize[0];
                    cLineWidth = 0
                    cLineStart += FONT_SIZE + 2
                    
                    #If the line is full
                    if(cLineStart > self.size.y):
                        break
                    

                newTextObject = TextWord(self.truePos, Vec2(cLineWidth, cLineStart), word + " ", color = wordColor)
                
                cLineWidth = newLineWidth

                self.addWord(newTextObject)

                
    def addWord(self, word):
        word.setParentPos(self.truePos)
        self.words.append(word)

    def draw(self, renderer):
        super().draw(renderer)

        for word in self.words:
            word.draw(renderer)
        

