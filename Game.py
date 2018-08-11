import pygame
# from pygame.locals import *
import Entity


size = w, h = 320, 420

pygame.init()
screen = pygame.display.set_mode(size)


def main():
    done = False
    Dude = Entity.Default_Entity('(def)head.png', '(def)body.png', '(def)(L)arm.png', '(def)(R)arm.png', '(def)legs.png', (50, 50), None)
    Dude.add_bodypart()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        Dude.Run(screen)
        pygame.display.flip()


main()
