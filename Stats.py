import random
import Tool
import math
import enum 


Compass = {'+': 0, 'N': 1, 'NE': 2, 'E': 3, 'SE': 4, 'S': 5, 'SW': 6, 'W': 7, 'NW': 8}


class Stat(dict, object):
    pass


Fundamental = {}
Organic = {}
Organic["Integrity"] = 100
Organic["Relative Integrity"] = Tool.Unstable_Value(Organic["Integrity"], (Organic["Integrity"]-math.sqrt(Organic["Integrity"]), Organic["Integrity"]+math.sqrt(Organic["Integrity"])), 1)
Organic["Death"] = bool(Organic["Integrity"] == 0)

Being = Stat()
Being["Steps Taken"] = 0
Being["Max/Min Thought"] = Tool.Unstable_Value(50, (1, 100), 5)
Being["Tire_Rate"] = Tool.Bounded_Value(0, (-1, 1))
Being["Energy"] = Tool.Bounded_Value(100, (0, 110))
Being["Integrity"] = 100
Being["Movement Inclination"] = Tool.Unstable_Value(Compass['+'], (Compass['+'], 8), 1)
# ^should be removed since movement inclinations should be based on paths, areas, processing functions or general directions as well
