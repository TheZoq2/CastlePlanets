from gui import *

TEXT_SPECIAL_CHAR = "~"

textObjects = {
        "FOOD": "Resources/food.png",
        "IRON": "Resources/iron.png",
        "IRON_MAX": "Resources/ironMAX.png",
        "WOOD": "Resources/wood.png",
        "WOOD_MAX": "Resources/woodMax.png"
    }

baseFont = pygame.SysFont("", 16)

class TextWord(GUIElement):
    text = ""
    rendered = None

    def __init__(self, parentPos, pos, text):
        super.__init__(parentPos, pos)
        self.text = text

        rendered = baseFont.render(self.text, True, (255, 255, 255))

    def draw(self, renderer):
        super().draw(renderer)
        renderer.draw(self.rendered, self.truePos)

class TextObject(GUIElement):
    text = ""
    words = []

    def __init__(self, parentPos, pos, size, text):
        super().__init__(parentPos, pos)

        self.text = text
    
    def generateObjects():
        #Split text into words
        rawWords = text.split()

        for word in rawWords:
            if(word[0] == TEXT_SPECIAL_CHAR):

