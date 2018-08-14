import pygame
import os


def load_image(picdir):
    return pygame.image.load(picdir)


class Skeleton(list):
    def __init__(self):
        self.sockets = list()
        
    def add_part(self, params):
        self.append(Part(params))
    
    def list_parts(self):
        for i in range(len(self)):
            print("Section #" + str(i),  "--> " + self[i].name, "\t pos: " + str(self[i].pos))
    

class Part():
    def __init__(self, name, pos=(0, 0)):
        self.name = name
        self.pos = (0, 0)
    
    def set(self, pos):
        self.pos = pos


class Entity():
    def __init__(self, name, gfx, pos=(0, 0)):
        self.name = name
        self.gfx = load_image(gfx)
        self.pos = pos
        self.body = Skeleton()

    def create_body(self, *params):
        for i in range(len(params)):
            self.body.add_part(params[i])
    
    def arrange_parts(self, *params):
        for i in range(len(params)):
            self.body[i].set(params[i])

    def debug_body(self):
        print("\n\n------Entitiy: " + self.name + "-----")
        for i in range(len(self.body)):
            print(self.body[i].name + " pos: ", self.body[i].pos)

    def draw(self, screen):
        screen.blit(self.gfx, self.pos)
