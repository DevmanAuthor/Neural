import System
import pygame
import Tool
import UI
import Entity
import Director
import Creatures
import Image
from SubScenes import ControlBar, CentralMenu


class MainMenu(Director.Scene):
    def __init__(self, active=False):
        super(MainMenu, self).__init__(active)
        self.Buttons = dict()
        self.Background = Image.Sprite("gfx/UI/MenuBackground.png")
        self.load()

    def load(self): 
        ControlBar.load(self)
        CentralMenu.load(self)

    def handle_events(self, event):
        if "started" in CentralMenu.handle_events(self, event):
            self.change_scene(GameScene)
        if "cycle" in ControlBar.handle_events(self, event):
            self.change_scene(GameScene)

    def draw(self, sheet): 
        self.Background.draw(sheet)
        CentralMenu.draw(self, sheet)
        ControlBar.draw(self, sheet)
        

class Game_Scene(Director.Scene):
    def __init__(self, active=False):
        super(Game_Scene, self).__init__(active)
        self.Buttons = dict()
        self.load()

    def load(self): 
        ControlBar.load(self)
        
    def handle_events(self, event):
        if "cycle" in ControlBar.handle_events(self, event):
            self.change_scene(MainMenu)
 
    def draw(self, sheet):
        ControlBar.draw(self, sheet)
        

MainMenu = MainMenu(True)
GameScene = Game_Scene()


def update_scenes():
    return (MainMenu, GameScene)


List = update_scenes()