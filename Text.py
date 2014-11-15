from gui import *

TEXT_SPECIAL_CHAR = "~"

textObjects = {
        "FOOD": "

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
