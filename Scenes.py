import System
import pygame
import Tool
import UI
import Entity
import Director
import Creatures


class MainMenu(Director.Scene):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.Buttons = dict()
        self.Background = Tool.load_image("gfx/UI/MenuBackground.png")
        self.Load()

    def Load(self): 
        self.Buttons["Start"] = UI.Button(0, 0, "gfx/ball.png")
        self.Buttons["Start"].place((System.width/2)-self.Buttons["Start"].rect[2], (System.height/2)-self.Buttons["Start"].rect[3])
        self.Buttons["Toggle"] = UI.ToggleButton(0, 0, None, "OFF")
        print(self.Buttons["Start"].pos, System.width, System.height)

    def Handle_Events(self, event):
        if "clicked" in self.Buttons["Start"].handle_events(event):
            self.Buttons["Start"].set_text("Soon to be Implemented")
            self.Change_Scene(Game_Scene())
        retval = self.Buttons["Toggle"].handle_events(event)
        if "toggle_on" in retval:
            self.Buttons["Toggle"].set_text("ON")
        elif "toggle_off" in retval:
            self.Buttons["Toggle"].set_text("OFF")

        print(retval, self.Buttons["Toggle"].SWITCH)

    def Draw(self, sheet):
        System.screen.blit(self.Background, (0, 0))
        self.Buttons["Start"].draw(sheet)
        self.Buttons["Toggle"].draw(sheet)


class Game_Scene(Director.Scene):
    def __init__(self):
        super(Game_Scene, self).__init__()
        self.Buttons = dict()
        self.Load()

    def Load(self): 
        self.Buttons["Help"] = UI.Button(0, 0, "gfx/UI/help.png")
        self.Buttons["Help"].scale(20, 20, True, 1.5, 1.5)
        self.Buttons["Help"].place(System.screen.get_width()-(self.Buttons["Help"].rect.width+self.Buttons["Help"].reliefsize), 0)

        self.Buttons["Exit"] = UI.Button(0, 0, "gfx/UI/eyexit.png")
        self.Buttons["Exit"].scale(50, 40, True, 2, 2)
        self.Buttons["Exit"].place(System.width-self.Buttons["Exit"].rect.width-self.Buttons["Exit"].reliefsize, System.height-self.Buttons["Exit"].rect.height-self.Buttons["Exit"].reliefsize)
         
    def Handle_Events(self, event):
        if 'clicked' in self.Buttons["Help"].handle_events(event):
            self.nextscene = MainMenu()
        if 'clicked' in self.Buttons["Exit"].handle_events(event):
            System.Quit()
            
    def Draw(self, sheet):
        self.Buttons["Help"].draw(sheet)
        self.Buttons["Exit"].draw(sheet)
