import pygame
from pygame.locals import *
from planet import *

pygame.init()
screen = pygame.display.set_mode((1280, 700))
clock = pygame.time.Clock()

planets = [Planet(640, 350, 0)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    for planet in planets:
        planet.draw(screen)

    pygame.display.flip()
