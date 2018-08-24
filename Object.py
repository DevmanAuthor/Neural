import random
import Elements
import Tool


class Neuron():
    def __init__(self, initial_value, bounds, force):
        self.value = initial_value
        self.bounds = bounds
        self.force = force

    @property
    def value(self):
        self._value += random.randint(-self.force, self.force)
        self._value = Tool.clamp(self._value, self.bounds[0], self.bounds[1])
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Stats(dict):
    def __init__(self, args=""):
        self.update(args)


Integrity = 80
Satisfaction = 100
Health_Stats = (Integrity, Satisfaction)

Health_Average = Neuron((sum(Health_Stats)/2), (min(Health_Stats), 100), 5)

Elemental = {"Integrity": 100}

Bodylimb = {"Integrity": 100, "Strength": 10, "Flexibility": 10, "Reflexiveness": 10}


class Basic():
    def __init__(self, name, stats=Stats()):
        self.name = name
        self.stats = stats
        self.Composition = ""

    def set(self, statname, value):
        self.stats[statname] = value

    def debug_self(self):
        return (self.name + " " + str(self.stats))


class Basic_gfx(Basic):
    def __init__(self, name, stats=Stats(), pos=(0, 0), gfx="./ball.png"):
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





