import UI
import Object
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
        Creatures.Load()
        for i in range(len(args)):
            for key, value in args[i]:
                self.add(key, value)

    def add(self, item, laynum):
        self.layers[laynum].append(item)

    def draw(self, screen):
        for l in range(self.layersize):
            for i in range(len(self.layers[l])):
                if isinstance(self.layers[l][i], Entity.Basic_gfx):
                    self.layers[l][i].draw(screen)

    def debug_layers(self):
        listofobj = "-----Layers: " + str(self.layersize) + "----------\n" + str(self.layers) + "\n-------------------------\n\n"
        for i in range(self.layersize):
            for j in range(len(self.layers[i])):
                listofobj += "Layer Position: " + str([i][j]) + self.layers[i][j].debug_self()
        return listofobj

    def Run(self, screen):
        self.draw(screen)
    