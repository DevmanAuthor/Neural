import pygame
from pygame.locals import *
import System
import Stats
import Entity
import Tool
import pygbutton
import Image
        

class Text(Image.Sprite, Tool.Simple, object):
    def __init__(self, string, color=System.WHITE, font=System.Default_Font, pos=(0, 0)):
        self.font = font
        self.color = color
        self.pos = pos
        self.str = str(string)
        self._gfx = self.font.render(self.str, True, self.color)

    def get_gfx(self):
        return self._gfx
        
    def set_gfx(self, size=None):
        if size is None:
            self._gfx = self.font.render(self.str, True, self.color)
        else:
            self._gfx = pygame.transform.scale(self._gfx, )
    
    def set_text(self, string):
        self.str = str(string)

    gfx = property(get_gfx, set_gfx)


class Button(Tool.Simple, object):
    def __init__(self, x=0, y=0, overlay=None, text=None, font=System.Default_Font, normal="gfx/UI/Natural/BtnNormal.png", pressed="gfx/UI/Natural/BtnNormal.png", hover="gfx/UI/Natural/BtnHover.png"):
        super(Button, self).__init__(x, y)
        self._font = font
        self.normal = Image.Sprite(normal)
        self.pressed = Image.Sprite(pressed)
        self.hover = Image.Sprite(hover)
        self.size = (self.normal.gfx.get_width(), self.normal.gfx.get_height())
        self.overlay = overlay
        self.set_rect(0, 0, 0, 0)
        
        self.isbuttonPressed = False
        self.isbuttonHovered = False
        self.lastMouseevent = False
        self.text = None
        self.reliefsize = 3

        if overlay is not None:
            self.set_overlay(overlay)
        if text is not None:
            self.set_text(text)

    def set_rect(self, x, y, w, h):
        self._rect = pygame.Rect(x, y, w, h) 

    def set_text(self, string, font=pygame.font.SysFont(None, 15), color=System.BLACK):
        self.text = Text(string, color, font)
        self.text.pos = (self.rect.centerx-self.text.gfx.get_width(), self.rect.centery-self.text.gfx.get_height())
        
        self.scale(self.text.gfx.get_rect().width+self.reliefsize+10, self.text.gfx.get_rect().height+self.reliefsize+10)
        
    def set_reliefsize(self, size):
        self.reliefsize = size

    def set_overlay(self, string, w=None, h=None):
        self.overlay = Image.Sprite(string)
        if w is not None and h is not None:
            self.scale_overlay(w, h)

    def fix_overlay(self):
        self.overlay.gfx = pygame.transform.scale(self.overlay, (self.scale_he, self.scale_we))

    def handle_events(self, event):
        retval = []
        if event.type not in [MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION]:
            return []
        else:
            if not self.isbuttonHovered and self._rect.collidepoint(event.pos):
                self.isbuttonHovered = True
                retval.append('entered')
            elif self.isbuttonHovered and not self._rect.collidepoint(event.pos):
                self.isbuttonHovered = False
                retval.append('exited')

            if self._rect.collidepoint(event.pos) and event.type == MOUSEBUTTONDOWN:
                self.isbuttonPressed = True
                retval.append("pressed")
                self.lastMouseevent = True
            if self.isbuttonPressed and event.type == MOUSEBUTTONUP:
                self.isbuttonPressed = False
                retval.append("released")

            doMouseclick = False
            if event.type == MOUSEBUTTONUP:
                if self.lastMouseevent:
                    doMouseclick = True
                self.lastMouseevent = False

            if doMouseclick:
                retval.append("clicked")

        return retval

    def get_rect(self):
        self._rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        return self._rect

    def draw(self, sheet):
        if self.isbuttonPressed:
            self.size = (self.pressed.gfx.get_width(), self.pressed.gfx.get_height())
            sheet.blit(self.pressed.gfx, self.rect)
            self.draw_relief(sheet, self.rect, "pressed")

        elif self.isbuttonHovered:
            self.size = (self.hover.gfx.get_width(), self.hover.gfx.get_height())
            sheet.blit(self.hover.gfx, self.rect)
            self.draw_relief(sheet, self.rect, "hover")

        else:
            self.size = (self.normal.gfx.get_width(), self.normal.gfx.get_height())
            sheet.blit(self.normal.gfx, self.rect)
            self.draw_relief(sheet, self.rect, "normal")

        if self.overlay is not None:
            sheet.blit(self.overlay.gfx, Tool.center(self.overlay.gfx.get_size(), self.rect))
        
        if self.text is not None:
            sheet.blit(self.text.gfx, Tool.center(self.text.gfx.get_size(), self.rect))        

    def scale(self, w, h, overscale=False, w2=1, h2=1):
        scale = (int(w/w2), int(h/h2))
        self.normal.gfx = pygame.transform.scale(self.normal.gfx, (w, h))
        self.pressed.gfx = pygame.transform.scale(self.normal.gfx, (w, h))
        self.hover.gfx = pygame.transform.scale(self.normal.gfx, (w, h))
        if overscale and self.overlay is not None:
            self.scale_overlay(w2, h2)
        self.size = (w, h)

    def scale_overlay(self, w, h):
        w = int(self.normal.gfx.get_width()/w)
        h = int(self.normal.gfx.get_height()/h)
        self.overlay.gfx = pygame.transform.scale(self.overlay.gfx, (w, h))

    def fix_text(self):
        self.text.set_gfx((self.rect[2]-self.reliefsize, self.rect[3]-self.reliefsize))

    def draw_relief(self, sheet, rect, style):
        x, y, xx, yy = rect[0], rect[1], rect[0]+rect[2], rect[1]+rect[3]
        if style == "normal":
            pygame.draw.line(sheet, System.LIGHTGRAY, (x, y), (x, yy), self.reliefsize)
            pygame.draw.line(sheet, System.LIGHTGRAY, (x, y), (xx, y), self.reliefsize) 
            pygame.draw.line(sheet, System.DARKGRAY, (xx, yy), (xx, y), self.reliefsize)
            pygame.draw.line(sheet, System.DARKGRAY, (xx, yy), (x, yy), self.reliefsize)
        elif style == "pressed":
            pygame.draw.line(sheet, System.LIGHTGRAY, (xx, yy), (xx, y), self.reliefsize)
            pygame.draw.line(sheet, System.LIGHTGRAY, (xx, yy), (x, yy), self.reliefsize)
            pygame.draw.line(sheet, System.DARKGRAY, (x, y), (x, yy), self.reliefsize)
            pygame.draw.line(sheet, System.DARKGRAY, (x, y), (xx, y), self.reliefsize) 
        elif style == "hover":
            pygame.draw.line(sheet, System.LIGHTGRAY, (x, y), (x, yy), self.reliefsize)
            pygame.draw.line(sheet, System.LIGHTGRAY, (x, y), (xx, y), self.reliefsize) 
            pygame.draw.line(sheet, System.DARKGRAY, (xx, yy), (xx, y), self.reliefsize)
            pygame.draw.line(sheet, System.DARKGRAY, (xx, yy), (x, yy), self.reliefsize)

    rect = property(get_rect, set_rect)


class SwitchButton(Button):
    def __init__(self, Toggle=False, x=0, y=0, overlay=None, text=None, font=System.Default_Font, normal="gfx/UI/Natural/BtnNormal.png", pressed="gfx/UI/Natural/BtnNormal.png", hover="gfx/UI/Natural/BtnHover.png"):
        super(SwitchButton, self).__init__(x, y, overlay, text, font, normal, pressed, hover)
        self.Toggle = Toggle

    def handle_events(self, event):
        retval = []
        if event.type not in [MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION]:
            return []
        else:
            if not self.isbuttonHovered and self.rect.collidepoint(event.pos):
                self.isbuttonHovered = True
                retval.append('entered')
            elif self.isbuttonHovered and not self.rect.collidepoint(event.pos):
                self.isbuttonHovered = False
                retval.append('exited')

            if self._rect.collidepoint(event.pos) and event.type == MOUSEBUTTONDOWN:
                self.isbuttonPressed = True
                retval.append("pressed")
                self.lastMouseevent = True
            if self.isbuttonPressed and event.type == MOUSEBUTTONUP:
                self.isbuttonPressed = False
                retval.append("released")

            doMouseclick = False
            if event.type == MOUSEBUTTONUP:
                if self.lastMouseevent:
                    doMouseclick = True
                self.lastMouseevent = False
     
            if doMouseclick:
                if self.Toggle is True:
                    retval.append("off")
                    self.Toggle = False
                elif self.Toggle is False:
                    retval.append("on")
                    self.Toggle = True
                retval.append("clicked")
                
        return retval

    def draw(self, sheet):   
        if self.Toggle is True:
            self.size = (self.pressed.gfx.get_width(), self.pressed.gfx.get_height())
            sheet.blit(self.pressed.gfx, self.rect)
            self.draw_relief(sheet, self.rect, "pressed")
        elif self.Toggle is False:
            self.size = (self.normal.gfx.get_width(), self.normal.gfx.get_height())
            sheet.blit(self.normal.gfx, self.rect)
            self.draw_relief(sheet, self.rect, "normal")
                
        if self.overlay is not None:
            sheet.blit(self.overlay.gfx, Tool.center(self.overlay.gfx.get_size(), self.rect))
        if self.text is not None:
            sheet.blit(self.text.gfx, Tool.center(self.text.gfx.get_size(), self.rect))


class ToggleButton(SwitchButton):
    def __init__(self, Toggle=False, x=0, y=0, overlay=None, text=None, font=System.Default_Font, normal="gfx/UI/Natural/BtnNormal.png", pressed="gfx/UI/Natural/BtnNormal.png", hover="gfx/UI/Natural/BtnHover.png"):
        super(ToggleButton, self).__init__(Toggle, x, y, overlay, text, font, normal, pressed, hover)

    def draw(self, sheet):
        Button.draw(self, sheet)