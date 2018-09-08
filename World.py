import UI
import Entity
import Creatures
import pygame


class World():
    def __init__(self, size, numoflayers=10):
        self.size = size
        self.layersize = numoflayers
        self.layers = [0] * numoflayers
        for i in range(len(self.layers)):
            self.layers[i] = list()
        
    def load(self, *args):
        for i in range(len(args)):
            for key, value in args[i].items():
                self.add(key, value)

    def add(self, item, laynum):
        self.layers[laynum].append(item)

    def draw(self, sheet):
        for l in range(self.layersize):
            for i in range(len(self.layers[l])):
                if isinstance(self.layers[l][i], Entity.Drawable_Object):
                    self.layers[l][i].draw(sheet)

    def debug_layers(self):
        layercontents = "-----Layers: " + str(self.layersize) + "----------\n" + str(self.layers) + "\n-------------------------\n\n"
        return layercontents

    def debug_entities(self):
        listofobj = self.debug_layers()
        for i in range(self.layersize):
            for j in range(len(self.layers[i])):
                listofobj += "Layer Position: " + str([i][j]) + self.layers[i][j].debug_self()
        return listofobj

    def Run(self, sheet):
        self.draw(sheet)
    