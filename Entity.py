import pygame
import os
import Tool
import random
import Stats


class Drawable_Object():
    pass


class Basic():
    def __init__(self, name, stats=Stats.Fundamental):
        self.name = name
        self.stats = stats
        self.Composition = ""

    def set(self, statname, value):
        self.stats[statname] = value

    def debug_self(self):
        return (self.name + " " + str(self.stats))


class Basic_gfx(Basic, Drawable_Object):
    def __init__(self, name, stats=Stats.Fundamental, pos=(0, 0), gfx="./ball.png"):
        super(Basic_gfx, self).__init__(name, stats)
        self.gfx = Tool.load_image(gfx)
        self.pos = pos
        self.stats = stats

    def place(self, pos):
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.gfx, self.pos)
    
    def debug_self(self):
        return (self.name + " " + str(self.pos) + " " + self.stats)


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
        listoflimbs = str()
        for i in range(len(self)):
            listoflimbs += "Section #" + str(i) + "--> " + self[i].debug_self() + "\n"
        return listoflimbs

    def arrange_limbs(self, *params):
        for i in range(len(params)):
            self[i].place(params[i])


class Limb(Basic):
    def __init__(self, *args, stats=Stats.Organic):
        super(Limb, self).__init__(*args)
        self.stats = stats


class Brain(Limb):
    def __init__(self, *args):
        super(Brain, self).__init__(*args)

    def Dream(self, body):
        pass
    
    def Determine_Movement():
        pass


class Organism(Basic_gfx):
    def __init__(self, *args):
        super(Organism, self).__init__(*args)
        self.body = Skeleton()
        self.body.add_brain("Brain")
        self.Composition = ""
    
    def debug_self(self):
        return ("\n|=========[ " + self.name + " ]=========|\n" + ":---> " + str(self.pos) + " " + str(self.stats) + "\n\n" + self.body.list_limbs() + "\n|==============================================================|")

    def Run(self):
        self.body[0].Dream(self.body)