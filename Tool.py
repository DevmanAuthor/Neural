import pygame
import sys


def tup_sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def merge_dict(a, b):
    return {**a, **b}


def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n


def load_image(picdir):
    return pygame.image.load(picdir)