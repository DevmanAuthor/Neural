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
        self.Load()

    def Load(self): 
        ControlBar.Load(self)
        CentralMenu.Load(self)

    def Handle_Events(self, event):
        if "started" in CentralMenu.Handle_Events(self, event):
            self.Change_Scene(GameScene)
        if "cycle" in ControlBar.Handle_Events(self, event):
            self.Change_Scene(GameScene)

    def Draw(self, sheet): 
        self.Background.draw(sheet)
        CentralMenu.Draw(self, sheet)
        ControlBar.Draw(self, sheet)
        

class Game_Scene(Director.Scene):
    def __init__(self, active=False):
        super(Game_Scene, self).__init__(active)
        self.Buttons = dict()
        self.Load()

    def Load(self): 
        ControlBar.Load(self)
        
    def Handle_Events(self, event):
        if "cycle" in ControlBar.Handle_Events(self, event):
            self.Change_Scene(MainMenu)
 
    def Draw(self, sheet):
        ControlBar.Draw(self, sheet)
        

MainMenu = MainMenu(True)
GameScene = Game_Scene()


def Update_Scenes():
    return (MainMenu, GameScene)


List = Update_Scenes()