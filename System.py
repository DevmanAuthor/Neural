import sys
import pygame
# from pygame.locals import *
import Stats
import Entity
import World
import Creatures
import Elements
import Menu
import UI


width, height = 640, 480

screen = pygame.display.set_mode((width, height))
render_layer = pygame.Surface((width/2, height/2))
World = World.World((400, 400))


def Load():
    Creatures.Load()
    Menu.Load()
    World.load(Creatures.List)
    print(World.debug_layers())


def Run():
    while True:
        
        UI.text.update(Stats.Organic["Health Aura"].value)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
            Menu.Update(event)
        
        Draw()
        print(Stats.Organic["Health Aura"].value)
    
    
def Draw():
    pygame.transform.scale2x(render_layer, screen)
    Menu.draw(screen)
    UI.text.draw(screen)
    World.Run(screen)
    pygame.display.flip()


def Quit():
        pygame.display.quit()
        pygame.quit()
        sys.exit()