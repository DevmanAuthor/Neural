import pygame
# from pygame.locals import *
import Object
import Entity
import World
import Creatures


size = w, h = 640, 480

pygame.init()
screen = pygame.display.set_mode(size)
render_layer = pygame.Surface((320, 240))

RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)


def main():
    done = False
    
    World1 = World.World((400, 400), 3)
    World1.load(Creatures.BugBear)
    print(World1.debug_layers(0))
    Creatures.BugBear.Compose_Matter("AAABBC", "AABBCC", "aeoeiqnf", "Cheeky")
    print(Creatures.BugBear.Composition)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
       
        pygame.transform.scale2x(render_layer, screen)
        World1.draw(screen)
        pygame.display.flip()


main()
