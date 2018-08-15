import pygame
import os

DEFSTAT = (10, 10, 10, 10, 10)


def load_image(picdir):
    return pygame.image.load(picdir)


class Skeleton(list):
    def __init__(self):
        self.sockets = list()
        
    def add_part(self, params):
        self.append(Part(params))
    
    def list_parts(self):
        for i in range(len(self)):
            print("Section #" + str(i),  "--> " + self[i].name, "\t pos: " + str(self[i].pos))
    

class Stats():
    def __init__(self, s):
        self.integrity = s[0]
        self.strength = s[1]
        self.flexibility = s[2]
        self.energy = s[3]
        self.responsivenss = s[4]


class Part():
    def __init__(self, name, pos=(0, 0)):
        self.name = name
        self.pos = pos
        self.stats = Stats(DEFSTAT)
    
    def set(self, pos):
        self.pos = pos


class Brain(Part):
    def __init__(self, *args):
        Part.__init__(self, *args)

    def Dream(self, Skeleton):
        pass


class Entity():
    def __init__(self, name, gfx, pos=(0, 0)):
        self.name = name
        self.gfx = load_image(gfx)
        self.pos = pos
        self.body = Skeleton()
        
    def create_body(self, *params):
        for i in range(len(params)):
            self.body.add_part(params[i])
    
    def arrange_parts(self, *params):
        for i in range(len(params)):
            self.body[i].set(params[i])

    def debug_body(self):
        print("\n\n------Entitiy: " + self.name + "-----")
        for i in range(len(self.body)):
            print(self.body[i].name + " pos: ", self.body[i].pos)
       
    def draw(self, screen):
        screen.blit(self.gfx, self.pos)


class Mover(Entity):
    pass