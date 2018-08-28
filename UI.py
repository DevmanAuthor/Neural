import pygame
from pygame.locals import *
import Stats
import Creatures
import Entity
import Tool
import pygbutton

pygame.init()

WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)


class Text():
    def __init__(self, font, txt, color=WHITE, pos=(0, 0)):
        self.font = font
        self.color = color
        self.pos = pos
        self.str = str(txt)

    def draw(self, sheet):
        self.obj = self.font.render(self.str, True, self.color)
        sheet.blit(self.obj, self.pos)
    
    def update(self, string):
        self.str = str(string)


class Button(pygbutton.PygButton):
    def __init__(self,  *args):
        super(Button, self).__init__(*args)
        self.pos = (self._rect.x, self._rect.y)
    
    def move(self, pos):
        self._pos = tuple((self._pos[0] + pos[0], self._pos[1] + pos[1]))
        r = pygame.Rect(self._pos[0], self._pos[1], self._rect[2], self._rect[3])
        self._propSetRect(r)
    
    def set_pos(self, pos):
        self._pos = pos
    
    def get_pos(self):
        return self._pos

    pos = property(get_pos, set_pos)
    

text = Text(pygame.font.SysFont(None, 18), Stats.Organic["Health Aura"].value)

HUD = {text: 9}
