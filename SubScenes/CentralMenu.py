import System
import pygame
import Image
import Tool
import UI


def load(self): 
    self.Menu_Frame = Image.Sprite("gfx/UI/menuback.png", (50, 50))
    self.Menu_Frame.scale(200, 230)
    self.Menu_Frame.pos = Tool.center(self.Menu_Frame.gfx.get_size(), System.screen.get_rect())

    self.Buttons["Start"] = UI.Button()
    self.Buttons["Start"].set_text("Start", pygame.font.Font("font/homespun.ttf", 15))
    self.Buttons["Start"].place(System.width/2-self.Buttons["Start"].rect[2]/2, System.height/2-(self.Buttons["Start"].rect[3]/2)*6)

    self.Buttons["Sound"] = UI.ToggleButton(True)
    self.Buttons["Sound"].scale(20, 20, True, 1.2, 1.2)
    self.Buttons["Sound"].place(50, 50)


def handle_events(self, event):
    retval = []
    if "clicked" in self.Buttons["Start"].handle_events(event):
        retval.append("started")
    ev = self.Buttons["Sound"].handle_events(event)
    if self.Buttons["Sound"].SWITCH is True:
        self.Buttons["Sound"].set_overlay("gfx/UI/sound_on.png", 1.2, 1.2)
    elif self.Buttons["Sound"].SWITCH is False:
        self.Buttons["Sound"].set_overlay("gfx/UI/sound_off.png", 1.2, 1.2)
    return retval


def draw(self, sheet):
    self.Menu_Frame.draw(sheet)
    Image.Decor.draw(sheet, 0, self.Menu_Frame.pos)
    self.Buttons["Start"].draw(sheet)
    self.Buttons["Sound"].draw(sheet)
  