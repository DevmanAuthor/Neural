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
    guy = Entity.Entity("Default", "gfx/none.png")
    guy.create_body('Head', 'Torso', 'Arms', 'Legs')
    guy.arrange_parts((10, 10), (20, 13), (82, 10))
    guy.body.append(Entity.Brain("Brain", (12, 10)))
    guy.body.list_parts()
    print(guy.body[4].name, guy.body[4].pos)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
       
        pygame.transform.scale2x(render_layer, screen)
        guy.draw(render_layer)
        # guy.debug_body()
        pygame.display.flip()


main()
