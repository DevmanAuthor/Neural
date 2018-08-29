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
        self.obj = self.font.render(self.str, True, self.color)

    def draw(self, sheet):
        self.obj = self.font.render(self.str, True, self.color)
        sheet.blit(self.obj, self.pos)
    
    def update(self, string):
        self.str = str(string)


class Button(pygbutton.PygButton):
    def __init__(self,  *args):
        super(Button, self).__init__(*args)
        self.pos = (self._rect.x, self._rect.y)
        self.overlay = None
    
    def center(self, sheet):
        return (self._rect.centerx - sheet.get_width()/2, self._rect.centery - sheet.get_height()/2)

    def move(self, change):
        self._pos = tuple((self._pos[0] + change[0], self._pos[1] + change[1]))
        r = pygame.Rect(self._pos[0], self._pos[1], self._rect[2], self._rect[3])
        self._propSetRect(r)

    def add_overlay(self, gfx):
        self.overlay = Tool.load_image(gfx)
    
    def add_text(self, font, string, color=BLACK):
        self.text = Text(font, string, color)
        self.text.pos = self.center(self.text.obj)

    def draw(self, sheet):
        super(Button, self).draw(sheet)
        if self.overlay is not None:
            sheet.blit(self.overlay, self.center(self.overlay))
        if self.text is not None:
            sheet.blit(self.text.obj, self.center(self.text.obj))

    def set_pos(self, pos):
        self._pos = pos
    
    def get_pos(self):
        return self._pos

    pos = property(get_pos, set_pos)
    

text = Text(pygame.font.SysFont(None, 18), Stats.Organic["Health Aura"].value)

HUD = {text: 9}
