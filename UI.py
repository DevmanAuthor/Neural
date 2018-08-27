import pygame
from pygame.locals import *
import Stats
import Creatures
import Entity
import Tool
pygame.init()

WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)


class Text(Entity.Drawable_Object):
    def __init__(self, font, txt, color=WHITE, pos=(0, 0)):
        self.font = font
        self.color = color
        self.pos = pos
        self.str = str(txt)

    def draw(self, screen):
        self.obj = self.font.render(self.str, True, self.color)
        screen.blit(self.obj, self.pos)
    
    def update(self, string):
        self.str = str(string)


class Button(Entity.Drawable_Object):
    def __init__(self, pos, string, font=pygame.font.SysFont(None, 18)):
        self.pos = pos
        self.txt = textobj(font, string, BLACK)
        self.gfx = list()
        self.rect = pygame.rect()
        self.lastMouseoverButton = False
    
    def set_surfaces(self, normal, pressed, hover=0, overlay=0):
        self.gfx.extend(normal, pressed, hover)
        self.rect = self.gfx[0].get_rect()

    def on_mousemotion(self, event):
        pass

    def on_mousedown(self, event):
        pass

    def handle_event(self, event):
        if event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return []

        retval = []
        hasExited = False
        if self._rect.collidepoint(event):
            if event.type == MOUSEMOTION and self.gfx[3] != 0:
                self.on_mousemotion(event)
                retval.append('motion')
            elif event.type == MOUSEBUTTONDOWN:
                self.buttondown = True
                self.lastMouseoverButton = True
                self.on_mousedown(event)
                retval.append('down')
        else:
            if event.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
                self.lastMouseoverButton = False
        
        doMouseClick = False
        if event.type == MOUSEBUTTONUP:
            if self.lastMouseoverButton:
                doMouseClick = True
            self.lastMouseoverButton = False
            if self.buttondown:
                self.buttondown = False
            if doMouseClick:
                retval.append('click')
                self.mouseclick(event)

        if hasExited:
            self.on_mouseexit(event)
            retval.append('exit')
        
        return retval
        
    def update(self):
        pass
    
    
text = Text(pygame.font.SysFont(None, 18), Stats.Organic["Health Aura"].value)


HUD = {text: 9}
