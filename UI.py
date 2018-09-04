import pygame
from pygame.locals import *
import System
import Stats
import Creatures
import Entity
import Tool
import pygbutton

pygame.init()


class Text(object):
    def __init__(self, string, color=System.WHITE, font=pygame.font.SysFont(None, 15), pos=(0, 0)):
        self.font = font
        self.color = color
        self.pos = pos
        self.str = str(string)
        self._obj = self.font.render(self.str, True, self.color)

    def get_obj(self):
        return self._obj
        
    def set_obj(self, size=None):
        if size is None:
            self._obj = self.font.render(self.str, True, self.color)
        else:
            self._obj = pygame.transform.scale(self._obj, size)

    def draw(self, sheet):
        sheet.blit(self.obj, self.pos)
    
    def update(self, string):
        self.str = str(string)

    obj = property(get_obj, set_obj)


class Button(object):
    def __init__(self, x=0, y=0, overlay=None, text=None, font=pygame.font.SysFont(None, 12), normal="gfx/UI/Natural/BtnNormal.png", pressed="gfx/UI/Natural/BtnNormal.png", hover="gfx/UI/Natural/BtnHover.png"):
        self.pos = (x, y)
        self._font = font
        self.normal_gfx = Tool.load_image(normal)
        self.pressed_gfx = Tool.load_image(pressed)
        self.hover_gfx = Tool.load_image(hover)
        self.currentsize = (self.normal_gfx.get_width(), self.normal_gfx.get_height())
        self.place(x, y)
        self.overlay_gfx = overlay
        
        self.buttonPressed = False
        self.buttonHovered = False
        self.lastMouseevent = False
        self.text = None
        self.reliefsize = 3

        if overlay is not None:
            self.load_overlay(overlay)
        if text is not None:
            self.set_text(text)
    
    def set_text(self, string, font=pygame.font.SysFont(None, 15), color=System.BLACK):
        self.text = Text(string, color, font)
        self.text.pos = (self.rect.centerx-self.text.obj.get_width(), self.rect.centery-self.text.obj.get_height())
        
        self.scale(self.text.obj.get_rect().width+self.reliefsize+10, self.text.obj.get_rect().height+self.reliefsize+10)
        
    def set_reliefsize(size):
        self.reliefsize = size

    def load_overlay(self, string, w=None, h=None):
        self.overlay_gfx = Tool.load_image(string)
        if w is not None and h is not None:
            self.scale_overlay(w, h)

    def fix_overlay(self):
        self.overlay_gfx = pygame.transform.scale(self.overlay_gfx, (self.scale_he, self.scale_we))

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

    def move(self, x, y):
        self.pos = (self.pos[0]+x, self.pos[1]+y)
        
    def place(self, x, y):
        self.pos = (x, y)

    def get_rect(self):
        self._rect = pygame.Rect(self.pos[0], self.pos[1], self.currentsize[0], self.currentsize[1])
        return self._rect

    def draw(self, sheet):
        if self.buttonPressed:
            self.currentsize = (self.pressed_gfx.get_width(), self.pressed_gfx.get_height())
            sheet.blit(self.pressed_gfx, self.rect)
            self.draw_relief(sheet, self.rect, "pressed")

        elif self.buttonHovered:
            self.currentsize = (self.hover_gfx.get_width(), self.hover_gfx.get_height())
            sheet.blit(self.hover_gfx, self.rect)
            self.draw_relief(sheet, self.rect, "hover")

        else:
            self.currentsize = (self.normal_gfx.get_width(), self.normal_gfx.get_height())
            sheet.blit(self.normal_gfx, self.rect)
            self.draw_relief(sheet, self.rect, "normal")

        if self.overlay_gfx is not None:
            sheet.blit(self.overlay_gfx, Tool.center(self.overlay_gfx, self.rect))
        
        if self.text is not None:
            sheet.blit(self.text.obj, Tool.center(self.text.obj, self.rect))        

    def scale(self, w, h, overscale=False, w2=1, h2=1):
        scale = (int(w/w2), int(h/h2))
        self.normal_gfx = pygame.transform.scale(self.normal_gfx, (w, h))
        self.pressed_gfx = pygame.transform.scale(self.normal_gfx, (w, h))
        self.hover_gfx = pygame.transform.scale(self.normal_gfx, (w, h))
        if overscale and self.overlay_gfx is not None:
            self.scale_overlay(w2, h2)
        self.currentsize = (w, h)

    def scale_overlay(self, w, h):
        w = int(self.normal_gfx.get_width()/w)
        h = int(self.normal_gfx.get_height()/h)
        self.overlay_gfx = pygame.transform.scale(self.overlay_gfx, (w, h))

    def fix_text(self):
        self.text.set_obj((self.rect[2]-self.reliefsize, self.rect[3]-self.reliefsize))

    def draw_relief(self, sheet, rect, style):
        x, y, xx, yy = rect[0], rect[1], rect[0]+rect[2], rect[1]+rect[3]
        if style == "normal":
            pygame.draw.line(sheet, System.LIGHTGRAY, (x, y), (x, yy-1), self.reliefsize)
            pygame.draw.line(sheet, System.LIGHTGRAY, (x, y), (xx-1, y), self.reliefsize) 
            pygame.draw.line(sheet, System.DARKGRAY, (xx, yy), (xx, y-1), self.reliefsize)
            pygame.draw.line(sheet, System.DARKGRAY, (xx, yy), (x-1, yy), self.reliefsize)
        elif style == "pressed":
            pygame.draw.line(sheet, System.DARKGRAY, (x, y), (x, yy-1), self.reliefsize)
            pygame.draw.line(sheet, System.DARKGRAY, (x, y), (xx-1, y), self.reliefsize) 
            pygame.draw.line(sheet, System.LIGHTGRAY, (xx, yy), (xx, y-1), self.reliefsize)
            pygame.draw.line(sheet, System.LIGHTGRAY, (xx, yy), (x-1, yy), self.reliefsize)
        elif style == "hover":
            pygame.draw.line(sheet, System.LIGHTGRAY, (x, y), (x, yy-1), self.reliefsize)
            pygame.draw.line(sheet, System.LIGHTGRAY, (x, y), (xx-1, y), self.reliefsize) 
            pygame.draw.line(sheet, System.DARKGRAY, (xx, yy), (xx, y-1), self.reliefsize)
            pygame.draw.line(sheet, System.DARKGRAY, (xx, yy), (x-1, yy), self.reliefsize)

    rect = property(get_rect)


class ToggleButton(Button):
    def __init__(self, x=0, y=0, overlay=None, text=None, font=pygame.font.SysFont(None, 12), normal="gfx/UI/Natural/BtnNormal.png", pressed="gfx/UI/Natural/BtnNormal.png", hover="gfx/UI/Natural/BtnHover.png"):
        super(ToggleButton, self).__init__(x, y, overlay, text, font, normal, pressed, hover)
        self.SWITCH = False
        self.doMouseclick = False

    def handle_events(self, event):
        retval = []
        if event.type not in [MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION]:
            return []
        else:
            if not self.buttonHovered and self.rect.collidepoint(event.pos):
                self.buttonHovered = True
                retval.append('entered')
            elif self.buttonHovered and not self.rect.collidepoint(event.pos):
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
                if self.SWITCH is True:
                    retval.append("toggle_off")
                    self.SWITCH = False
                elif self.SWITCH is False:
                    retval.append("toggle_on")
                    self.SWITCH = True
                retval.append("clicked")
                
        return retval

    def draw(self, sheet):      
        if self.SWITCH is True:
            self.currentsize = (self.pressed_gfx.get_width(), self.pressed_gfx.get_height())
            sheet.blit(self.pressed_gfx, self.rect)
            self.draw_relief(sheet, self.rect, "pressed")
        elif self.SWITCH is False:
            self.currentsize = (self.normal_gfx.get_width(), self.normal_gfx.get_height())
            sheet.blit(self.normal_gfx, self.rect)
            self.draw_relief(sheet, self.rect, "normal")
        if self.buttonHovered:
            pass
            
        if self.overlay_gfx is not None:
            sheet.blit(self.overlay_gfx, Tool.center(self.overlay_gfx, self.rect))
        if self.text is not None:
            sheet.blit(self.text.obj, Tool.center(self.text.obj, self.rect))


text = Text(Stats.Organic["Health Aura"].value)

HUD = {text: 9}
