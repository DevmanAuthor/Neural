import random
import Tool
import math


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


Fundamental = {}


Organic = {}
Organic["Integrity"] = 100
Organic["Relative Integrity"] = (Organic["Integrity"]-math.sqrt(Organic["Integrity"]), Organic["Integrity"]+math.sqrt(Organic["Integrity"]))
Organic["Pain"] = 3
Organic["Nutrition"] = 90
Organic["Stability"] = random.randint((Organic["Relative Integrity"][0] + Organic["Relative Integrity"][1])/2, Organic["Integrity"])
Organic["Death"] = bool(Organic["Integrity"] == 0)
Organic["Health Aura"] = Neuron(Organic["Integrity"], (Organic["Relative Integrity"][0] - Organic["Pain"], Organic["Integrity"]), 1)

Being = {}
Being["Max/Min Thought"] = [0, 100]
Being["Integrity"] = 100
Being["Pain"] = 0
Being["Hunger"] = 10
Being["Mental Stability"] = random.randint(0, Being["Integrity"])
Being["Health Actual"] = int((Being["Integrity"] - Being["Pain"]) - (Being["Hunger"]/3))
Being["Health Sentiment"] = Being["Health Actual"] + random.randint(0, 100)
Being["Movement Inclination"] = Neuron(Being["Health Sentiment"] / 8, (0, 8), 1)
