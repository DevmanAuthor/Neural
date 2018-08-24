import pygame
import os
import Object
import Tool
import random


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


class Limb(Object.Basic):
    def __init__(self, *args, stats=Object.Stats()):
        super(Limb, self).__init__(*args)
        self.stats = stats


class Brain(Limb):
    def __init__(self, *args):
        super(Brain, self).__init__(*args)

    def Dream(self, body):
        pass


class Organism(Object.Basic_gfx):
    def __init__(self, *args):
        super(Organism, self).__init__(*args)
        self.body = Skeleton()
        self.body.add_brain("Brain")
        self.Composition = ""
    
    def debug_self(self):
        return ("\n|=========[ " + self.name + " ]=========|\n" + ":---> " + str(self.pos) + " " + str(self.stats) + "\n\n" + self.body.list_limbs() + "\n|==============================================================|")

    def Run(self):
        self.body[0].Dream(self.body)