import pygame
import sys


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


def load_image(picdir): return pygame.image.load(picdir)


def pyrect_sub(rect, value): return pygame.Rect(rect[0]-value, rect[1]-value, rect[2]-value, rect[3]-value)


def pyrect_extend(rect, value): return pygame.Rect(rect[0]+value, rect[1]+value, rect[2]+value, rect[3]+value)