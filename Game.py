import sys
import pygame
# from pygame.locals import *
import System
import Director
import Stats
import Entity
import World
import Elements
import Scenes
import UI
import Tool
import Image


SceneManager = Director.SceneManager(Scenes.List)


def Run():
    System.screen.fill(System.BLACK)
    while SceneManager is not None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                System.Quit()
            SceneManager.handle_events(event)
        System.time = System.checktime()
        SceneManager.check_active()
        SceneManager.update()
        pygame.transform.scale2x(System.render_sheet, System.screen)
        SceneManager.draw(System.screen)
        pygame.display.flip()
    

Run()