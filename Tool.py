import pygame


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


def intersection(a, b):
    c = a.intersection(b)
    return c


def intersect(a, b):
    return set(set(substring(a)) & set(substring(b)))


def substring(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            yield s[i: j+1]

 
def load_image(picdir):
    return pygame.image.load(picdir)