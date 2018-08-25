import pygame
import Stats
import Creatures
import Entity
pygame.init()


class textobj(Entity.Drawable_Object):
    def __init__(self, font, string, color=(225, 225, 255), pos=(0, 0)):
        self.font = font
        self.color = color
        self.pos = pos
        self.str = string

    def draw(self, screen):
        self.obj = self.font.render(self.str, True, self.color)
        screen.blit(self.obj, self.pos)
    
    def update(self, string):
        self.str = string


class Button(Entity.Drawable_Object):
    pass
        

default_font = pygame.font.SysFont(None, 18)
text = textobj(default_font, "sup")


HUD = {text: 9}
