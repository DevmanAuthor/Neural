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
    Creatures.BugBear.Compose_Matter("AAABBC", "AABBCC", "aeoeiqnf", "Cheeky")
    Creatures.BugBear.body.create("Head", "Torso", "Arm")
    
    Creatures.BugBear.Run()
    print(World1.debug_layers(0))
    print(Creatures.BugBear.Composition)
    n = Object.Neuron(10, (0, 20), 5)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
       
        pygame.transform.scale2x(render_layer, screen)
        World1.draw(screen)
        print(Object.Health_Average.value)
        pygame.display.flip()


main()
