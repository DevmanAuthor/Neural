import random
import Elements
import Tool
import json
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
    string.lower()
    return dict(Counter(string.replace(' ', '')))
 

def match_compound(compound, string):
    if compound == evaluate_element(string):
        return True
    else:
        return False


def filter_(x, y):
    count = 0
    for num in y:
        if num in x:
            count += 1
    return count


def generate_compounds(string):
    str_cnt = Counter(string)
    comp = ""
    for key, value in Elements.List.items():
        e_cnt = Counter(Elements.List[key])
        if (e_cnt & str_cnt) == e_cnt:
            comp += (key + ".")
    print(comp)
    
    
def generate_compound(string, elm):
    s = Counter(string)
    e = Counter(elm)
    mixed_set = s & e
    count = 0
    comp = ''
    l = list()
    print("this is i:", mixed_set, "\nthis is s: ", s)
    
    for keys in mixed_set:
        keysval = s.get(keys)
        print(keys, keysval)
        l.append(keysval)

    times_to_put = 0
    for k in e:
        for i in range(len(l)):
            if l[i] % e.get(k) == 0:
                times_to_put += 1

    comp = (elm + ".") * times_to_put
    print(comp, l)


def foof(j, i, s):
    pass


def break_down_compound(dictry):
    s = str()
    for key, val in dictry.items():
        s += str(key) * dictry[key]
    return s


def break_down_element(string):
    s = str()
    d = evaluate_element(string)
    d = break_down_compound(d)
    return d


class Stats(dict):
    def __init__(self, args):
        self.update(args)


Integrity = 80
Satisfaction = 100
Health_Stats = (Integrity, Satisfaction)

Health_Average = Neuron((sum(Health_Stats)/2), (min(Health_Stats), 100), 5)

Elemental = {"Integrity": 100}

Bodylimb = {"Integrity": 100, "Strength": 10, "Flexibility": 10, "Reflexiveness": 10}


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
        pass


def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n




