import System
import UI


def Load(self): 
    self.Buttons["Start"] = UI.Button(0, 0, "gfx/ball.png")
    self.Buttons["Start"].place((System.width/2)-self.Buttons["Start"].rect[2], (System.height/2)-self.Buttons["Start"].rect[3])
    self.Buttons["Sound"] = UI.ToggleButton(0, 0, None, "DISABLED")


def Handle_Events(self, event):
    retval = []
    if "clicked" in self.Buttons["Start"].handle_events(event):
        self.Buttons["Start"].set_text("Soon to be Implemented")
        retval.append("started")
    ev = self.Buttons["Sound"].handle_events(event)
    if "toggle_on" in ev:
        self.Buttons["Sound"].set_text("DISABLED")
    elif "toggle_off" in ev:
        self.Buttons["Sound"].set_text("ENABLED")
    return retval


def Draw(self, sheet):
    System.screen.blit(self.Background, (0, 0))
    self.Buttons["Start"].draw(sheet)
    self.Buttons["Sound"].draw(sheet)