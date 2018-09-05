import System
import pygame
import Tool
import UI


def Load(self): 
    self.frame = UI.Frame("gfx/UI/menuback.png", (50, 50))
    self.Buttons["Start"] = UI.Button()
    self.Buttons["Start"].set_text("Start", pygame.font.Font("font/homespun.ttf", 20))
    self.frame.pos = Tool.center(self.frame.gfx.get_size(), System.screen.get_rect())
    self.Buttons["Start"].place(System.width/2-self.Buttons["Start"].rect[2]/2, System.height/2-self.Buttons["Start"].rect[3]/2)

    self.Buttons["Sound"] = UI.ToggleButton(True, 0, 0, "gfx/UI/sound_on.png")
    self.Buttons["Sound"].scale(30, 30, True, 1.2, 1.2)
 

def Handle_Events(self, event):
    retval = []
    if "clicked" in self.Buttons["Start"].handle_events(event):
        retval.append("started")
    ev = self.Buttons["Sound"].handle_events(event)
    if "toggle_on" in ev:
        self.Buttons["Sound"].load_overlay("gfx/UI/sound_on.png", 1.2, 1.2)
    elif "toggle_off" in ev:
        self.Buttons["Sound"].load_overlay("gfx/UI/sound_off.png", 1.2, 1.2)
    return retval


def Draw(self, sheet):
    self.frame.draw(sheet)
    self.Buttons["Start"].draw(sheet)
    self.Buttons["Sound"].draw(sheet)
  