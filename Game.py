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
import Image


SceneManager = Director.SceneManager(Scenes.List)


def Run():
    System.screen.fill(System.BLACK)
    while SceneManager is not None:
        Scenes.Update_Scenes()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                System.Quit()
            SceneManager.Handle_Scene_Events(event)

        SceneManager.check_active()
        pygame.transform.scale2x(System.render_sheet, System.screen)
        SceneManager.Draw(System.screen)
        pygame.display.flip()
    

Run()