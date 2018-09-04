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


class scenes(lists, object):
    pass


scene_s = scenes()


def Run():
    System.screen.fill(System.BLACK)
    activescene = Scenes.MainMenu()
    scene_s.append(Scenes.MainMenu)
    while activescene is not None:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                System.Quit()
            activescene.Handle_Events(event)  

        for i in range(len(scene_s)):
            if scene_s[i].active is False:
                scene_s[i].pop(scene_s[i])
            else:
                scene_s[i].Draw(System.screen)

        activescene = activescene.nextscene
        pygame.transform.scale2x(System.render_sheet, System.screen)
        activescene.Draw(System.screen)
        pygame.display.flip()
    

Run()