import pygame
# from pygame.locals import *
import Guy


size = w, h = 320, 420

pygame.init()
screen = pygame.display.set_mode(size)

Dude = Guy.Guy('(def)head.png', '(def)body.png', '(def)(L)arm.png', '(def)(R)arm.png', '(def)legs.png')


def main():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        '''
        screen.blit(Dude.head.gfx, (50, 50))
        screen.blit(Dude.arm_r.gfx, (50+8, 50+8))
        screen.blit(Dude.arm_l.gfx, (50-8, 50+8))
        screen.blit(Dude.body.gfx, (50, 50+8))
        screen.blit(Dude.legs.gfx, (50, 50+8+8))
        '''
        Dude.pos = (50, 50)
        Dude.Run(screen)
        pygame.display.flip()


main()
