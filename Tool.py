import pygame
import sys
import Tool
import random


class Simple():
    def __init__(self, x, y):
        self.place(x, y)

    def place(self, x, y):
        self.pos = (x, y) 

    def set_pos(self, pos):
        self.pos = pos

    def move(self, x, y):
        self.pos = (self.pos[0] + x, self.pos[1] + y)


class ComplexValue():
    pass


class Bounded_Value(ComplexValue):
    def __init__(self, val, bounds):
        self.value = val
        self.bounds = bounds

    @property
    def value(self):
        self._value = Tool.clamp(self._value, self.bounds[0], self.bounds[1])
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Unstable_Value(ComplexValue):
    def __init__(self, val, bounds, force):
        self.value = val
        self.bounds = bounds
        self.force = force

    @property
    def value(self):
        self._value += random.randint(-self.force, self.force)
        self._value = Tool.clamp(self._value, self.bounds[0], self.bounds[1])
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


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
        return (rect.centerx - size[0]/2, rect.centery - size[1]/2)


def stepoffcenter(size, rect, x, y):
        pos = center(size, rect)
        return stepoff(size, pos, x, y)


def stepoff(size, pos, x, y):
        if x == 0:
            xx = pos[0]
        else:
            xx = pos[0] + size[0] * x
        if y == 0:
            yy = pos[1]
        else:
            yy = pos[1] + size[1] * y    
        return (xx, yy)


def load_image(picdir): return pygame.image.load(picdir)


def pyrect_sub(rect, value): return pygame.Rect(rect[0]-value, rect[1]-value, rect[2]-value, rect[3]-value)


def pyrect_extend(rect, value): return pygame.Rect(rect[0]+value, rect[1]+value, rect[2]+value, rect[3]+value)


def pos_clamp(bounds, point, factor):
    x, y = point[0], point[1]
    if point[0] <= bounds[0]:
        x += factor
    if point[1] <= bounds[1]:
        y += factor
    if point[0] >= bounds[2]:
        x -= factor
    if point[1] >= bounds[3]:
        y -= factor
    return (x, y)