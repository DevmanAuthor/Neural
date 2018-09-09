import pygame
import os
import Tool
import random
import Stats
import Image
import System


class Basic(Tool.Simple):
    def __init__(self, name, stats=Stats.Fundamental):
        self.name = name
        self.stats = stats
        self.Composition = ""

    def set(self, statname, value):
        self.stats[statname] = value

    def debug_self(self):
        return (self.name + " " + str(self.stats))


class Basic_Drawable(Basic, Image.Sprite):
    def __init__(self, name, stats=Stats.Fundamental, pos=(0, 0), gfx="gfx/ball.png"):
        Basic.__init__(self, name, stats)
        Image.Sprite.__init__(self, gfx, pos)

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
        self.signal = None

    def recieve(self, signal):
        self.signal = signal

    def send(self, node, signal):
        node.recieve(signal)


class Brain(Limb):
    def __init__(self, *args):
        super(Brain, self).__init__(*args)

    def dream(self, body):
        return random.randint(-1000, 1000)


class Organism(Basic_Drawable):
    def __init__(self, name, stats=Stats.Fundamental, pos=(0, 0), gfx="gfx/ball.png"):
        super(Organism, self).__init__(name, stats, pos, gfx)
        self.body = Skeleton()
        self.body.add_brain("Brain")
        self.mind = self.body[0]
        self.Composition = ""
        self.bounds = pygame.Rect(0, 0, System.width, System.height)

    def travel(self):
        if self.bounds.collidepoint(self.pos):
            print("value: ", self.stats["Movement Inclination"].value)
            self.pos = Tool.tup_add(self.pos, self.determine_velocity(self.stats["Movement Inclination"].value, 1))
        else:
            self.pos = Tool.pos_clamp(self.bounds, self.pos, 1)

    def determine_velocity(self, i, factor):
        if i == Stats.Compass["+"]:
            return (0, 0)
        elif i == Stats.Compass["N"]:
            return (0, -factor)
        elif i == Stats.Compass["NE"]:
            return (factor, -factor)
        elif i == Stats.Compass["E"]:
            return (factor, 0)
        elif i == Stats.Compass["SE"]:
            return (factor, factor)
        elif i == Stats.Compass["S"]:
            return (0, factor)
        elif i == Stats.Compass["SW"]:
            return (-factor, factor)
        elif i == Stats.Compass["W"]:
            return (-factor, 0)
        elif i == Stats.Compass["NW"]:
            return (-factor, -factor)

    def debug_self(self):
        return ("\n|=========[ " + self.name + " ]=========|\n" + ":---> " + str(self.pos) + " " + str(self.stats) + "\n\n" + self.body.list_limbs() + "\n|==============================================================|")

    def run(self):
        self.mind.dream(self.body)
        self.travel()
        
        print("pos: ", self.pos)
        print("tire_rate: ", self.stats.tire_rate.value)
        print("Energy: ", self.stats["Energy"])