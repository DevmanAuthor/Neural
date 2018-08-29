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


class Button():
    def __init__(self, x, y, rect=pygame.Rect(50, 50, 10, 10), gfx=("gfx/UI/BtnNormal.png", "gfx/UI/BtnPressed.png", "gfx/UI/BtnHover.png", "gfx/Ball.png")):
        self.pos = self.set_pos(x, y)
        self._rect = rect
        self.gfx = [None, None, None, None]
        self.load_surfaces(gfx)
        self._rect.move_ip(x, y)
        
        self.buttonPressed = False
        self.buttonHovered = False
        self.lastMouseevent = False
        
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
                self.gfx[i] = (Tool.load_image(sheets[i]))
        self._rect = self.gfx[0].get_rect()
    
    def set_pos(self, x, y):
        self.pos = (x, y)

    def draw(self, sheet):
        # print(self.gfx)
        if self.gfx[3] is not None:
            sheet.blit(self.gfx[3], self._rect)

        if self.buttonPressed:
            sheet.blit(self.gfx[1], self._rect)
        elif self.buttonHovered and self.gfx[2] is not None:
            sheet.blit(self.gfx[2], self._rect)
        else:
            sheet.blit(self.gfx[0], self._rect)


text = Text(pygame.font.SysFont(None, 18), Stats.Organic["Health Aura"].value)

HUD = {text: 9}
