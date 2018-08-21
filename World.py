import Object
import Entity


class World():
    def __init__(self, size, numoflayers):
        self.size = size
        self.layers = [0] * numoflayers
        for i in range(len(self.layers)):
            self.layers[i] = list()
        
    def load(self):
        self.layers[0].append(Entity.Organism("dude", "gfx/none.png"))
        self.layers[0][0].place((50, 23))
        self.layers[0].append(123)
        self.layers[0].append(Entity.Organism("duder", "gfx/none.png"))
        self.layers[0].append(1233333)
        self.layers[0].append(Entity.Organism("dude", "gfx/none.png"))

    def draw(self, screen):
        for i in range(len(self.layers[0])):
            if isinstance(self.layers[0][i], Entity.Basic):
                self.layers[0][i].draw(screen)
        pass

    def Run(self):
        pass
        
    def debug_self(self):
        print(self.layers[0])
