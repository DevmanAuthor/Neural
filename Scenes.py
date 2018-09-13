import System
import pygame
import Tool
import UI
import Entity
import Director
import Image
from SubScenes.Scenes import CentralMenu, ControlBar, GameView


class MainMenu(Director.Scene):
    def __init__(self, active=False):
        super(MainMenu, self).__init__(active)
        self.Buttons = dict()
        self.Background = Image.Sprite("gfx/UI/MenuBackground.png")
        self.load()

    def update(self):
        pass

    def load(self):
        CentralMenu.load()
        ControlBar.load()

    def handle_events(self, event):
        if "started" in CentralMenu.handle_events(event):
            self.change_scene(GameScene)
        if "cycle" in ControlBar.handle_events(event):
            self.change_scene(GameScene)

    def draw(self, sheet):
        self.Background.draw(sheet) 
        CentralMenu.draw(sheet)
        ControlBar.draw(sheet)
        
  
class GameScene(Director.Scene):
    def __init__(self, active=False):
        super(GameScene, self).__init__(active)
        self.Buttons = dict()
        self.load()

    def load(self):
        ControlBar.load()
        GameView.load()

    def update(self):
        pass

    def handle_events(self, event):
        if "cycle" in ControlBar.handle_events(event):
            self.change_scene(MainMenu)

    def draw(self, sheet):
        ControlBar.draw(sheet)
        GameView.draw(sheet)


MainMenu = MainMenu(True)
GameScene = GameScene()


def update_scenes():
    return (MainMenu, GameScene)


List = update_scenes()