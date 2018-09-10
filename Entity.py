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

    def get_formated_stats(self):
        self._stats_formatted = self.format_stats()
        return self._stats_formatted

    def set_formated_stats(self):
        self._stats_formatted = self.format_stats()

    def format_stats(self):
        stats_actual = dict()
        for key, val in self.stats.items():
            if isinstance(val, Tool.ComplexValue):
                stats_actual.update({key: val.value})
            else:
                stats_actual.update({key: val})
        s = str(stats_actual)
        s = s.replace('{', '[')
        s = s.replace('}', ']')
        s = s.replace('\'', '')
        return s

    def debug_self(self):
        return (self.name + ": " + " " + self.stats_formatted)

    stats_formatted = property(get_formated_stats, set_formated_stats)


class Basic_Drawable(Basic, Image.Sprite):
    def __init__(self, name, stats=Stats.Fundamental, pos=(0, 0), gfx="gfx/ball.png"):
        Basic.__init__(self, name, stats)
        Image.Sprite.__init__(self, gfx, pos)

    def debug_self(self):
        return (self.name + " " + str(self.pos) + " " + self.stats_formatted)


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

    def debug_self(self):
        return ("\n|=========[ " + self.name + " ]=========|\n" + ":---> " + str(self.pos) + " " + self.stats_formatted + "\n\n" + self.body.list_limbs() + "\n|==============================================================|")

    def run(self):
        self.mind.dream(self.body)


class Walkable(Organism):
    def __init__(self, name, stats=Stats.Being, pos=(0, 0), gfx="gfx/guy.png"):
        super(Walkable, self).__init__(name, stats, pos, gfx)
        self.bounds = pygame.Rect(0, 0, System.width, System.height)

    def manage_stats(self):
        self.stats["Energy"] += self.stats["Tire_Rate"].value
        if self.stats["Max/Min Thought"].value < 50:
            self.stats["Tire_Rate"].value += 0.01
        else:
            self.stats["Tire_Rate"].value -= 0.01

    def travel(self):
        if self.bounds.collidepoint(self.pos):
            # print("value: ", self.stats["Movement Inclination"].value)
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
        return super(Walkable, self).debug_self() 

    def run(self):
        super(Walkable, self).run()
        self.manage_stats()
        self.travel()
        
        print(self.debug_self())