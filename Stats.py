import random
import Tool
import math
import enum 


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


Compass = {'+': 0, 'N': 1, 'NE': 2, 'E': 3, 'SE': 4, 'S': 5, 'SW': 6, 'W': 7, 'NW': 8}


class Stat(dict, object):
    pass


Fundamental = {}
Organic = {}
Organic["Integrity"] = 100
Organic["Relative Integrity"] = (Organic["Integrity"]-math.sqrt(Organic["Integrity"]), Organic["Integrity"]+math.sqrt(Organic["Integrity"]))
Organic["Pain"] = 3
Organic["Nutrition"] = 90
Organic["Stability"] = random.randint((Organic["Relative Integrity"][0] + Organic["Relative Integrity"][1])/2, Organic["Integrity"])
Organic["Death"] = bool(Organic["Integrity"] == 0)
Organic["Health Aura"] = Neuron(Organic["Integrity"], (Organic["Relative Integrity"][0] - Organic["Pain"], Organic["Integrity"]), 1)

Being = Stat()
Being["Max/Min Thought"] = Neuron(50, (0, 100), 5)
Being.tire_rate = Neuron(0, (-1, 1), int(Being["Max/Min Thought"].value/50))
# Being["Energy"] = Being.tire_rate.value
Being["Integrity"] = 100
Being["Movement Inclination"] = Neuron(Compass['+'], (Compass['+'], 8), 1)
# ^should be removed since movement inclinations should be based on paths, areas, processing functions or general directions as well
