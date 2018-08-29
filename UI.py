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
    def __init__(self, string, color=WHITE, font=pygame.font.SysFont(None, 15), pos=(0, 0)):
        self.font = font
        self.color = color
        self.pos = pos
        self.str = str(string)
        self._obj = self.font.render(self.str, True, self.color)

    def get_obj(self):
        self._obj = self.font.render(self.str, True, self.color)
        return self._obj
        
    def draw(self, sheet):
        sheet.blit(self.obj, self.pos)
    
    def update(self, string):
        self.str = str(string)

    obj = property(get_obj)


class Button():
    def __init__(self, x=0, y=0, overlay=None, gfx=("gfx/UI/BtnNormal.png", "gfx/UI/BtnPressed.png", "gfx/UI/BtnHover.png")):
        self.gfx = [None, None, None]
        self.pos = (x, y)
        self.load_surfaces(gfx)
        self._rect = self.get_rect()
        self.rect.move_ip(x, y)
        self.text = None
        self.buttonPressed = False
        self.buttonHovered = False
        self.lastMouseevent = False
        self.overlay = overlay
        if overlay is not None:
            self.overlay = Tool.load_image(overlay)
        
    def set_text(self, string, font=pygame.font.SysFont(None, 15), color=BLACK):
        self.text = Text(string, color, font)
        self.text.pos = (self.rect.centerx-self.text.obj.get_width()/4, self.rect.centery-self.text.obj.get_height()/4)

    def add_overlay(string):
        self.gfx[3] = Tool.load_image(string)

    def handle_events(self, event):
        retval = []
        if event.type not in [MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION]:
            return []
        else:
            if not self.buttonHovered and self._rect.collidepoint(event.pos):
                self.buttonHovered = True
                retval.append('entered')
            elif self.buttonHovered and not self._rect.collidepoint(event.pos):
                self.buttonHovered = False
                retval.append('exited')

            if self._rect.collidepoint(event.pos) and event.type == MOUSEBUTTONDOWN:
                self.buttonPressed = True
                retval.append("pressed")
                self.lastMouseevent = True
            if self.buttonPressed and event.type == MOUSEBUTTONUP:
                self.buttonPressed = False
                retval.append("released")

            doMouseclick = False
            if event.type == MOUSEBUTTONUP:
                if self.lastMouseevent:
                    doMouseclick = True
                self.lastMouseevent = False

            if doMouseclick:
                retval.append("clicked")

        return retval

    def load_surfaces(self, sheets):
        for i in range(len(sheets)):
            if sheets[i] is not None:
                self.gfx[i] = Tool.load_image(sheets[i])

    def move(self, x, y):
        self.pos = (self.pos[0]+x, self.pos[1]+y)
        
    def place(self, x, y):
        self.pos = (x, y)

    def get_rect(self):
        self._rect = pygame.Rect(self.pos[0], self.pos[1], self.gfx[0].get_width(), self.gfx[0].get_height())
        return self._rect

    def draw(self, sheet):
        if self.buttonPressed:
            sheet.blit(self.gfx[1], self.rect)
        elif self.buttonHovered and self.gfx[2] is not None:
            sheet.blit(self.gfx[2], self.rect)
        else:
            sheet.blit(self.gfx[0], self.rect)
        if self.overlay is not None:
            sheet.blit(self.overlay, self.center(self.overlay))
        
        if self.text is not None:
            sheet.blit(self.text.obj, self.center(self.text.obj))
    
    def scale(self, w, h, overscale=False):
        for i in range(3):
            if self.gfx[i] is not None:
                self.gfx[i] = pygame.transform.scale(self.gfx[i], (w, h))
        if overscale and self.overlay is not None:
            self.overlay = pygame.transform.scale(self.overlay, (int(w/2), int(h/2)))

    def center(self, obj):
        return (self.rect.centerx-obj.get_width()/2, self.rect.centery-obj.get_height()/2)
    
    rect = property(get_rect)
        

text = Text(Stats.Organic["Health Aura"].value)

HUD = {text: 9}
