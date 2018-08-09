import pygame
import os


class BodyPart:
    def __init__(self, gfx):
        self.gfx = gfx


class Guy:
    def __init__(self, head, body, arm_l, arm_r, legs):
        self.emotions = dict(shame=0, fear=0, pain=0, grief=0, joy=0, mood=0)
        self.head = BodyPart(pygame.image.load(os.path.join('gfx', head)))
        self.body = BodyPart(pygame.image.load(os.path.join('gfx'), body))
        self.arm_l = BodyPart(pygame.image.load(os.path.join('gfx'), arm_l))
        self.arm_r = BodyPart(pygame.image.load(os.path.join('gfx'), arm_r))
        self.legs = BodyPart(pygame.image.load(os.path.join('gfx'), legs))

    def Run(self):
        self.emotions.mood = (self.emotions.griefa / self.emotions.joy)
