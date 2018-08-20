import Object


class World():
    def __init__(self, size, numoflayers):
        self.size = size
        self.layers = [0] * numoflayers
