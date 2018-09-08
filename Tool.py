import pygame
import sys


class Simple():
    def __init__(self, x, y):
        self.place(x, y)

    def place(self, x, y):
        self.pos = (x, y) 

    def set_pos(self, pos):
        self.pos = pos

    def move(self, x, y):
        self.pos = (self.pos[0] + x, self.pos[1] + y)


def tup_sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def tup_add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def merge_dict(a, b):
    return {**a, **b}


def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n


def center(size, rect):
        return (rect.centerx-size[0]/2, rect.centery-size[1]/2)


def load_image(picdir): return pygame.image.load(picdir)


def pyrect_sub(rect, value): return pygame.Rect(rect[0]-value, rect[1]-value, rect[2]-value, rect[3]-value)


def pyrect_extend(rect, value): return pygame.Rect(rect[0]+value, rect[1]+value, rect[2]+value, rect[3]+value)