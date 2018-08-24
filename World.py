import Object
import Entity
import Creatures
import pygame


class World():
    def __init__(self, size, numoflayers):
        self.size = size
        self.layers = [0] * numoflayers
        for i in range(len(self.layers)):
            self.layers[i] = list()
        
    def load(self, *args):
        Creatures.Load()
        for i in args:
            self.layers[0].append(i)

    def draw(self, screen):
        for i in range(len(self.layers[0])):
            if isinstance(self.layers[0][i], Object.Basic):
                self.layers[0][i].draw(screen)
        
    def debug_layers(self, num):
        listofobj = str()
        for i in range(len(self.layers[num])):
            listofobj += str(self.layers[0][i]) + ": " + self.layers[0][i].debug_self()
        return listofobj

    def Run(self, screen):
        self.draw(screen)
    