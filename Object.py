import random
from collections import Counter


class Neuron():
    def __init__(self, initial_value, bounds, force):
        self.value = initial_value
        self.bounds = bounds
        self.force = force

    @property
    def value(self):
        self._value += random.randint(-self.force, self.force)
        self._value = clamp(self._value, self.bounds[0], self.bounds[1])
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

def evaluate_element(string):
    return dict(Counter(string.replace(' ', '')))


def determine_composition(compdict):
    
    pass


def determine_compound(compound, string):
    if tuple(compound) == evaluate_dna(string):
        return True
    else:
        return False


class Stats(dict):
    def __init__(self, args):
        self.update(args)


Integrity = 80
Satisfaction = 100
Health_Stats = (Integrity, Satisfaction)

Health_Average = Neuron((sum(Health_Stats)/2), (min(Health_Stats), 100), 5)

Elemental = {"Integrity": 100}

Bodylimb = {"Integrity": 100, "Strength": 10, "Flexibility": 10, "Reflexiveness": 10}

Compounds = {"Metal": (3, 2, 1), "Wood": (2, 2, 2), "Organic": (9, 9, 0)}
    
comp = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


class Basic():
    def __init__(self, name, stats=Stats(Elemental)):
        self.name = name
        self.stats = stats
        self.Composition = ""

    def set(self, statname, value):
        self.stats[statname] = value

    def debug_self(self):
        return (self.name + " " + str(self.stats))

    def Compose_Matter(self, *strs):
        for i in range(len(strs)):
            for key, value in Compounds.items():
                if determine_compound(Compounds[key], strs[i]):
                    self.Composition += (key + ".") 
                else:
                    pass


def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n




