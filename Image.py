import pygame
import System
import Tool


class Drawable():
    pass


class Sprite(Drawable, Tool.Simple, object):
    def __init__(self, gfx, pos=(0, 0)):
        self.load(gfx)
        self.pos = pos

    def load(self, gfx):
        if isinstance(gfx, str):
            self.filename = gfx
            self.gfx = Tool.load_image(gfx)
        else:
            self.gfx = gfx

    def draw(self, sheet, rect=None):
        if rect is None:
            sheet.blit(self.gfx, self.pos)
        else:
            sheet.blit(self.gfx, rect)

    def scale(self, w, h):
        self.gfx = pygame.transform.scale(self.gfx, (w, h))
        

class SpriteSheet():
    def __init__(self, filename, rects):
        self.sprite_file = Tool.load_image(filename)
        self.image = list()
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
            self.image.append(Sprite(self.get_image(rects[i])))
            self.image[i].place(rects[i][0], rects[i][1])

    def debug_sprite_sheet(self, sheet):
        for i in range(len(self.images)):
            pygame.draw.rect(self.images[i].gfx, System.RED, self.images[i].gfx.get_rect(), 2)
            self.image[i].draw(sheet)

    def draw(self, sheet, index, pos):
        sheet.blit(self.image[index].gfx, pos)

        
Decor = SpriteSheet("gfx/UI/decor_basic.png", ([0, 0, 16, 16], [16, 0, 16, 16]))