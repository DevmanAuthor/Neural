
num = 100
element = ("Air", "Water", "Earth", "Fire", "Light")

elemental = {"Name": None, "integrity": 100}
Bodylimb = {"Strength": 10, "Flex": 10}


class Stats(dict):
    def __init__(self, args):
        self.update(args)