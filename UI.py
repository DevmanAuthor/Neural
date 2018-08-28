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


class Button():
    def __init__(self, pos, string, font=pygame.font.SysFont(None, 18)):
        self.pos = pos
        self.txt = Text(font, string, BLACK)
        self.gfx = list()
        self._rect = pygame.Rect(0, 0, 0, 0)
        self.buttondown = False
        self.mouseover = False
        self.lastMouseDownoverButton = False
        
    def set_surfaces(self, normal, pressed, hover=0, overlay=0):
        self.gfx.append(Tool.load_image(normal))
        self.gfx.append(Tool.load_image(pressed))
        if hover != 0:
            self.gfx.append(Tool.load_image(hover))
        else:
            self.gfx.append(0)
        if overlay != 0:
            self.gfx.append(Tool.load_image(overlay))
        else:
            self.gfx.append(0)
        self._rect = self.gfx[0].get_rect()

    def move(self, pos):
        self.pos = pos
    
    def _get_rect():
        return pygame.Rect(self.pos[0], self.pos[1], self.gfx[0].get_width(), self.gfx[0].get_height())

    def _update_rect(newrect):
        self._rect = newrect

    def on_mouseenter(self, event):
        pass

    def on_mousemotion(self, event):
        pass

    def on_mousedown(self, event):
        pass

    def on_mouseexit(self, event):
        pass
        
    def on_mouseclick(self, event):
        pass

    def handle_event(self, event):
        if event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return []

        retval = []
        hasExited = False

        if not self.mouseover and self._rect.collidepoint(event.pos):
            self.mouseover = True
            self.on_mouseenter(event)
            retval.append('enter')
        elif self.mouseover and not self._rect.collidepoint(event.pos):
            self.mouseover = False
            hasExited = True
        
        if self._rect.collidepoint(event.pos):
            if event.type == MOUSEMOTION:
                self.on_mousemotion(event)
                retval.append('motion')
            elif event.type == MOUSEBUTTONDOWN:
                self.buttondown = True
                self.lastMouseDownoverButton = True
                self.on_mousedown(event)
                retval.append('down')
        else:
            if event.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
                self.lastMouseDownoverButton = False
        
        doMouseClick = False
        if event.type == MOUSEBUTTONUP:
            if self.lastMouseDownoverButton:
                doMouseClick = True
            self.lastMouseDownoverButton = False
            if self.buttondown:
                self.buttondown = False
            if doMouseClick:
                retval.append('click')
                self.on_mouseclick(event)

        if hasExited:
            self.on_mouseexit(event)
            retval.append('exit')
        
        return retval

    def update(self):
        pass
    
    def draw(self, sheet):
        if self.gfx[3] != 0:
            sheet.blit(self.gfx[3], self.pos)
        if self.buttondown:
            sheet.blit(self.gfx[1], self.pos)
        elif self.mouseover and self.gfx[2] != 0:
            sheet.blit(self.gfx[2])
        else:
            sheet.blit(self.gfx[0], self.pos)
    
    rect = property(_get_rect, _update_rect)


text = Text(pygame.font.SysFont(None, 18), Stats.Organic["Health Aura"].value)


HUD = {text: 9}
