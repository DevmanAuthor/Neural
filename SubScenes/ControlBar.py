import pygame
import System
import Tool
import UI


def load(self):
        self.Buttons["Cycle"] = UI.Button(0, 0, "gfx/ball.png")
        self.Buttons["Cycle"].scale(20, 20, True, 1.5, 1.5)
        self.Buttons["Cycle"].place(System.screen.get_width()-(self.Buttons["Cycle"].rect.width + self.Buttons["Cycle"].reliefsize), 0)

        self.Buttons["WindowControl"] = UI.ToggleButton(False, 0, 0, "gfx/UI/maximize.png", None, True)
        self.Buttons["WindowControl"].scale(20, 20, True, 1.5, 1.5)
        self.Buttons["WindowControl"].place(self.Buttons["Cycle"].pos[0] - self.Buttons["Cycle"].size[0], 0)


def handle_events(self, event):
        retval = []
        if 'clicked' in self.Buttons["Cycle"].handle_events(event):
            self.active = False
            retval.append("cycle")

        ev = self.Buttons["WindowControl"].handle_events(event)
        if 'on' in ev:
            System.screen = pygame.display.set_mode((System.width, System.height), pygame.FULLSCREEN)
        elif 'off' in ev:
            System.screen = pygame.display.set_mode((System.width, System.height))
        return retval


def draw(self, sheet):
        self.Buttons["Cycle"].draw(sheet)
        self.Buttons["WindowControl"].draw(sheet)

