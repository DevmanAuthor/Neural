import pygame
import os

sn = 20


class BodyPart:
    def __init__(self, gfx, pos=(0, 0), sockpoint=(0, 0)):
        self.pos = pos
        self.gfx = pygame.image.load(os.path.join('gfx', gfx))
        self.socket = sockpoint

    def lock_to(self, pos):
        self.pos = pos


class Guy:
    def __init__(self, head, body, arm_l, arm_r, legs, pos)
        self.pos = pos
        self.head = BodyPart(head)

        self.head.socket = (self.head.gfx.get_height()/2, self.head.gfx.get_width()/2)
        self.head.lock_to(self.pos)
        
        self.body = BodyPart(body)
        self.body.lock_to(self.head.pos)

        self.arm_l = BodyPart(arm_l)
        self.arm_r = BodyPart(arm_r)
        self.legs = BodyPart(legs)

    def Run(self, screen):
        screen.blit(self.head.gfx, self.head.pos)
        screen.blit(self.body.gfx, self.body.pos)
        print("\n\n\n Entity base position: ", self.pos)
        print("Head position: ", self.head.pos)
        print("Body position: ", self.body.pos)



