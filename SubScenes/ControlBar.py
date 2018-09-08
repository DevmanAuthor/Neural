import System
import UI


def load(self):
        self.Buttons["Cycle"] = UI.Button(0, 0, "gfx/ball.png")
        self.Buttons["Cycle"].scale(20, 20, True, 1.5, 1.5)
        self.Buttons["Cycle"].place(System.screen.get_width()-(self.Buttons["Cycle"].rect.width+self.Buttons["Cycle"].reliefsize), 0)

        self.Buttons["Exit"] = UI.Button(0, 0, "gfx/UI/eyexit.png")
        self.Buttons["Exit"].scale(40, 30, True, 1.4, 1.4)
        self.Buttons["Exit"].place(System.width-self.Buttons["Exit"].rect.width-self.Buttons["Exit"].reliefsize, System.height-self.Buttons["Exit"].rect.height-self.Buttons["Exit"].reliefsize)


def handle_events(self, event):
        retval = []
        if 'clicked' in self.Buttons["Cycle"].handle_events(event):
            self.active = False
            retval.append("cycle")
        if 'clicked' in self.Buttons["Exit"].handle_events(event):
            System.Quit()
        return retval


def draw(self, sheet):
        self.Buttons["Cycle"].draw(sheet)
        self.Buttons["Exit"].draw(sheet)

