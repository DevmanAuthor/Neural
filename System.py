import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGRAY = (64, 64, 64)
GRAY = (128, 128, 128)
LIGHTGRAY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
R_PINK = (255, 85, 255)


def Quit():
        pygame.display.quit()
        pygame.quit()
        sys.exit()


width, height = 640, 480
screen = pygame.display.set_mode((width, height))
render_sheet = pygame.Surface((width/2, height/2))

