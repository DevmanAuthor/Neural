import System
import pygame
import Tool
import UI
import Entity
import Director
import Creatures
from SceneList import ControlBar


class MainMenu(Director.Scene):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.Buttons = dict()
        self.Background = Tool.load_image("gfx/UI/MenuBackground.png")
        self.Load()

    def Load(self): 
        ControlBar.Load(self)
        self.Buttons["Start"] = UI.Button(0, 0, "gfx/ball.png")
        self.Buttons["Start"].place((System.width/2)-self.Buttons["Start"].rect[2], (System.height/2)-self.Buttons["Start"].rect[3])
        self.Buttons["Toggle"] = UI.ToggleButton(0, 0, None, "DISABLED")

    def Handle_Events(self, event):
        ControlBar.Handle_Events(self, event, Game_Scene())
        if "clicked" in self.Buttons["Start"].handle_events(event):
            self.Buttons["Start"].set_text("Soon to be Implemented")
            self.Change_Scene(Game_Scene())
        retval = self.Buttons["Toggle"].handle_events(event)
        if "toggle_on" in retval:
            self.Buttons["Toggle"].set_text("DISABLED")
        elif "toggle_off" in retval:
            self.Buttons["Toggle"].set_text("ENABLED")

    def Draw(self, sheet):
        System.screen.blit(self.Background, (0, 0))
        ControlBar.Draw(self, sheet)
        self.Buttons["Start"].draw(sheet)
        self.Buttons["Toggle"].draw(sheet)


class Game_Scene(Director.Scene):
    def __init__(self):
        super(Game_Scene, self).__init__()
        self.Buttons = dict()
        self.Load()

    def Load(self): 
        ControlBar.Load(self)
        
    def Handle_Events(self, event):
        ControlBar.Handle_Events(self, event, MainMenu())
 
    def Draw(self, sheet):
        ControlBar.Draw(self, sheet)
        
