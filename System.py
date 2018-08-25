import sys
import pygame
# from pygame.locals import *
import Object
import Entity
import World
import Creatures
import Elements

RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)


width, height = 640, 480

pygame.init()
screen = pygame.display.set_mode((width, height))
render_layer = pygame.Surface((width/2, height/2))
World = World.World((400, 400))


def Load():
    World.load(Creatures.List)
    print(World.debug_layers())


def Run():
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event.type = pygame.QUIT

        pygame.transform.scale2x(render_layer, screen)
        World.Run(screen)
        pygame.display.flip()