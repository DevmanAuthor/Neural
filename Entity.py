import pygame
import os
import Object
import Tool


class Skeleton(list):
    def __init__(self):
        self.sockets = list()
        
    def add_limb(self, params):
        self.append(Limb(params))
    
    def add_brain(self, params):
        self.append(Brain(params))

    def create(self, *params):
        for i in range(len(params)):
            self.add_limb(params[i])

    def list_limbs(self):
        for i in range(len(self)):
            print("Section #" + str(i),  "--> " + self[i].debug_self())

    def arrange_limbs(self, *params):
        for i in range(len(params)):
            self[i].place(params[i])


class Basic():
    def __init__(self, name, gfx=None, pos=(0, 0), stats=Object.Stats(Object.elemental)):
        self.name = name
        if gfx is not None:
            self.gfx = Tool.load_image(gfx)
        self.pos = pos
        self.stats = stats

    def place(self, pos):
        self.pos = pos

    def set(self, statname, value):
        self.stats[statname] = value

    def debug_self(self):
        return (self.name + "\t pos: " + str(self.pos) + "\t" + str(self.stats))
    
    def draw(self, screen):
        screen.blit(self.gfx, self.pos)


class Limb(Basic):
    def __init__(self, *args, stats=Object.Stats(Object.Bodylimb)):
        super(Limb, self).__init__(*args)
        self.stats = dict(stats)


class Brain(Limb):
    def Dream(self, Skeleton):
        pass


class Organism(Basic):
    def __init__(self, *args):
        super(Organism, self).__init__(*args)
        self.body = Skeleton()
    
    def debug_self(self):
        print("\n----------------------Entitiy: " + self.name + "---------------------------")
        super(Organism, self).debug_self()
        self.body.list_limbs()
        print("==============================================================")

    def draw(self, screen):
        screen.blit(self.gfx, self.pos)