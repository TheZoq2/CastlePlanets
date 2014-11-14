import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1280, 700))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
