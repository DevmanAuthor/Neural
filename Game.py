import pygame
# from pygame.locals import *
import Entity


size = w, h = 640, 480

pygame.init()
screen = pygame.display.set_mode(size)
render_layer = pygame.Surface((320, 240))

RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)


def main():
    done = False
    Dude = Entity.Guy("Dude", (50, 50))
    Dude.Load('gfx/Birdseye/(def)head.png', 'gfx/Birdseye/(def)torso.png', 'gfx/Birdseye/(def)(L)arm.png', 'gfx/Birdseye/(def)(R)arm.png', 'gfx/Birdseye/(def)(L)leg.png', 'gfx/Birdseye/(def)(R)leg.png')

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.transform.scale2x(render_layer, screen)
        Dude.Run(render_layer)
        pygame.display.flip()


main()
