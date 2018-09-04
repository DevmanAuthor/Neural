import System
import pygame
import UI


def Load(self): 
    self.Buttons["Start"] = UI.Button()
    self.Buttons["Start"].set_text("Start", pygame.font.Font("font/homespun.ttf", 20))
    self.Buttons["Start"].scale(80, 40)
    self.Buttons["Start"].place((System.width/2)-self.Buttons["Start"].rect[2], (System.height/2)-self.Buttons["Start"].rect[3]*4)

    self.Buttons["Sound"] = UI.ToggleButton(0, 0, "gfx/UI/sound_off.png")
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
    System.screen.blit(self.Background, (0, 0))
    self.Buttons["Start"].draw(sheet)
    self.Buttons["Sound"].draw(sheet)
  