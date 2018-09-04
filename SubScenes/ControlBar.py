import System
import UI


def Load(self):
        self.Buttons["Cycle"] = UI.Button(0, 0, "gfx/ball.png")
        self.Buttons["Cycle"].scale(20, 20, True, 1.5, 1.5)
        self.Buttons["Cycle"].place(System.screen.get_width()-(self.Buttons["Cycle"].rect.width+self.Buttons["Cycle"].reliefsize), 0)

        self.Buttons["Exit"] = UI.Button(0, 0, "gfx/UI/eyexit.png")
        self.Buttons["Exit"].scale(50, 40, True, 2, 2)
        self.Buttons["Exit"].place(System.width-self.Buttons["Exit"].rect.width-self.Buttons["Exit"].reliefsize, System.height-self.Buttons["Exit"].rect.height-self.Buttons["Exit"].reliefsize)


def Handle_Events(self, event):
        retval = []
        if 'clicked' in self.Buttons["Cycle"].handle_events(event):
            self.active = False
            retval.append("cycle")
        if 'clicked' in self.Buttons["Exit"].handle_events(event):
            System.Quit()
        return retval


def Draw(self, sheet):
        self.Buttons["Cycle"].draw(sheet)
        self.Buttons["Exit"].draw(sheet)

