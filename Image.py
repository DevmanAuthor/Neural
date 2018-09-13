import pygame
import System
import Tool


class Drawable():
    pass


class Sprite(Drawable, Tool.Simple):
    def __init__(self, gfx, pos=(0, 0)):
  
        self.gfx = self.load(gfx)
        self.lastx = None
        self.lasty = None
        self.pos = pos
        
    def get_rect(self):
        self._rect = pygame.Rect(self.pos[0], self.pos[1], self.gfx.get_width(), self.gfx.get_height())
        self.lastx = self._rect[0] + self._rect[2]
        self.lasty = self._rect[1] + self._rect[3]
        return self._rect         
    
    def load(self, gfx):
        if isinstance(gfx, str):
            return Tool.load_image(gfx)
        elif isinstance(gfx, pygame.Surface):
            self.gfx = gfx
        else:
            raise ValueError("gfx not string or surface")
   
    def draw(self, sheet, rect=None):
        if rect is None:
            sheet.blit(self.gfx, self.pos)
        else:
            sheet.blit(self.gfx, rect)

    def scale(self, w, h):
        self.gfx = pygame.transform.scale(self.gfx, (w, h))
        
    rect = property(get_rect)


class SpriteSheet(list, object):
    def __init__(self, filename, rects):
        self.sprite_file = Tool.load_image(filename)
        self.prepare(rects)
    
    def get_image(self, rect):
        pic = pygame.Surface([rect[2], rect[3]]).convert()
        pic.blit(self.sprite_file, (0, 0), rect)
        pic.set_colorkey(System.R_PINK, pygame.RLEACCEL)
        return pic

    def prepare(self, rects):
        for i in range(len(rects)): 
            print(rects[i])
            print(self.get_image(rects[i]))
            self.append(self.get_image(rects[i]))

    def debug_sprite_sheet(self, sheet):
        for i in range(len(self)):
            pygame.draw.rect(self.sprite_file, System.RED, self[i].get_rect(), 2)
            sheet.blit(self.sprite_file, (0, 0))

    def draw(self, sheet, index, pos):
        sheet.blit(self[index], pos)


class Tile(Sprite):
    def __init__(self, gfx):
        super(Tile, self).__init__(gfx)
        self.size = 32
        self.scale(self.size, self.size)


Decor = SpriteSheet("gfx/UI/decor_basic.png", ([0, 0, 16, 16], [16, 0, 16, 16]))