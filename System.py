import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)


class Empty(object):
    pass


def Quit():
        pygame.display.quit()
        pygame.quit()
        sys.exit()


width, height = 640, 480
screen = pygame.display.set_mode((width, height))
render_sheet = pygame.Surface((width/2, height/2))

