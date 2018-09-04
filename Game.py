import sys
import pygame
# from pygame.locals import *
import System
import Director
import Stats
import Entity
import World
import Creatures
import Elements
import Scenes
import UI
import Tool


def Run():
    System.screen.fill(System.BLACK)
    activescene = Scenes.MainMenu()
    while activescene is not None:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                System.Quit()
            activescene.Handle_Events(event)  

        activescene = activescene.nextscene
        pygame.transform.scale2x(System.render_sheet, System.screen)
        activescene.Draw(System.screen)
        pygame.display.flip()
    

Run()