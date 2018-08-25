import Object
import pygame
import Stats
import Creatures

pygame.init()
default_font = pygame.font.SysFont(None, 18)
text = None

HUD = ((text, 10))


def Update(screen):
    for i in HUD:
        for key, value in HUD[i]:
            pass
