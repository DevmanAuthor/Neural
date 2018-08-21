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
        listoflimbs = str()
        for i in range(len(self)):
            listoflimbs += "Section #" + str(i) + "--> " + self[i].debug_self() + "\n"
        return listoflimbs

    def arrange_limbs(self, *params):
        for i in range(len(params)):
            self[i].place(params[i])


class Basic():
    def __init__(self, name, stats=Object.Stats(Object.Elemental)):
        self.name = name
        self.stats = stats
        self.Composition = ""

    def set(self, statname, value):
        self.stats[statname] = value

    def debug_self(self):
        return (self.name + " " + str(self.stats))

    def Compose_Matter(self, *strs):
        for i in range(len(strs)):
            for key, value in Object.Compounds.items():
                if Object.determine_compound(Object.Compounds[key], strs[i]):
                    self.Composition += (key + ".") 
                else:
                    pass


class Basic_gfx(Basic):
    def __init__(self, name, stats=Object.Stats(Object.Elemental), pos=(0, 0), gfx="./ball.png"):
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


class Limb(Basic):
    def __init__(self, *args, stats=Object.Stats(Object.Bodylimb)):
        super(Limb, self).__init__(*args)
        self.stats = dict(stats)


class Brain(Limb):
    def Dream(self, Skeleton):
        pass


class Organism(Basic_gfx):
    def __init__(self, *args):
        super(Organism, self).__init__(*args)
        self.body = Skeleton()
        self.Composition = ""
    
    def debug_self(self):
        return ("\n|=========[ " + self.name + " ]=========|\n" + ":---> " + str(self.pos) + " " + str(self.stats) + "\n\n" + self.body.list_limbs() + "\n|==============================================================|")