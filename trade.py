import pygame

class Traderoute:
    def __init__(self, path, cargo):
        self.path = path
        self.cargo = cargo
        #print(path, len(path), len(path) - 1)

    def draw(self, renderer):
        for i in range(len(self.path) - 1):
            renderer.line(self.path[i].get_coords(), self.path[i+1].get_coords())
