import Object
import Entity


class World():
    def __init__(self, size, numoflayers):
        self.size = size
        self.layers = [0] * numoflayers
        for i in range(len(self.layers)):
            self.layers[i] = list()
        
    def load(self):
        self.layers[0].append(Entity.Organism("Some Guy", Object.elemental, (50, 50), "gfx/guy.png"))
        self.layers[0][0].body.create("head", "shoulders", "knees", "toes")
        self.layers[0].append(123)

    def draw(self, screen):
        for i in range(len(self.layers[0])):
            if isinstance(self.layers[0][i], Entity.Basic):
                self.layers[0][i].draw(screen)
        
    def debug_layers(self, num):
        listofobj = str()
        for i in range(len(self.layers[num])):
            listofobj += str(self.layers[0][i]) + " "
        return listofobj