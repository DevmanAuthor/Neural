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
    lim = Entity.Organism("dude", "gfx/none.png")
    lim.body.append(Entity.Brain("Brain"))
    lim.body.create("Head", "Torus", "Extenser")
    lim.body.arrange_limbs((14, 70), (80, 32))
    lim.body[1].set("Strength", 13)
    lim.debug_self()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
       
        pygame.transform.scale2x(render_layer, screen)
        screen.blit(lim.gfx, (150, 150))
        pygame.display.flip()


main()
