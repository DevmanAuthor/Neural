import pygame
import Tool
import UI
import System
import Image  
import Director


class CentralMenu(Director.Scene):
    def __init__(self, active=False):
        super(CentralMenu, self).__init__(active)
        self.Buttons = dict()
        self.load()

    def load(self): 
        self.Menu_Frame = Image.Sprite("gfx/UI/menuback.png", (50, 100))
        self.Menu_Frame.scale(160, 240)
        self.Buttons["Create"] = UI.Button()
        self.Buttons["Create"].set_text("Create", pygame.font.Font("font/homespun.ttf", 15))
        self.Buttons["Create"].set_pos(Tool.stepoffcenter((self.Buttons["Create"].size[0], self.Buttons["Create"].size[0]-4), self.Menu_Frame.rect, 0, -1))

        self.Buttons["Start"] = UI.Button()
        self.Buttons["Start"].set_text("Embark", pygame.font.Font("font/homespun.ttf", 15))
        self.Buttons["Start"].set_pos(Tool.stepoffcenter(self.Buttons["Start"].size, self.Menu_Frame.rect, 0, -1))

        self.Buttons["Sound"] = UI.ToggleButton(True, 0, 0, "gfx/UI/sound_on.png")
        self.Buttons["Sound"].scale(20, 20, True, 1.2, 1.2)
        self.Buttons["Sound"].set_pos(Tool.stepoffcenter(self.Buttons["Sound"].size, self.Menu_Frame.rect, -2, 4))

        self.Buttons["Exit"] = UI.Button(0, 0, "gfx/UI/eyexit.png")
        self.Buttons["Exit"].scale(20, 20, True, 1.2, 1.2)
        self.Buttons["Exit"].set_pos(Tool.stepoffcenter(self.Buttons["Sound"].size, self.Menu_Frame.rect, 2, 4))

    def handle_events(self, event):
        retval = []
        if "clicked" in self.Buttons["Create"].handle_events(event):
            pass
        if "clicked" in self.Buttons["Start"].handle_events(event):
            retval.append("started")
        if 'clicked' in self.Buttons["Exit"].handle_events(event):
            System.Quit()
        self.Buttons["Sound"].handle_events(event)

        if self.Buttons["Sound"].Toggle is True:
            self.Buttons["Sound"].set_overlay("gfx/UI/sound_on.png", 1.2, 1.2)
        elif self.Buttons["Sound"].Toggle is False:
            self.Buttons["Sound"].set_overlay("gfx/UI/sound_off.png", 1.2, 1.2)
        return retval

    def draw(self, sheet):
        self.Menu_Frame.draw(sheet)
        x = self.Menu_Frame.pos[0]
        y = self.Menu_Frame.pos[1]
        xx = self.Menu_Frame.lastx
        yy = self.Menu_Frame.lasty

        Image.Decor.draw(sheet, 0, (x, y))
        Image.Decor.draw(sheet, 0, (xx-Image.Decor[0].get_width(), y))
        Image.Decor.draw(sheet, 0, (x, yy-Image.Decor[0].get_height()))
        Image.Decor.draw(sheet, 0, (xx-Image.Decor[0].get_width(), yy-Image.Decor[0].get_height()))

        for i in range(int(self.Menu_Frame.gfx.get_width() / Image.Decor[1].get_width())-2):
            Image.Decor.draw(sheet, 1, Tool.stepoff(Image.Decor[0].get_size(), (x, y), i+1, 0))

        for i in range(int(self.Menu_Frame.gfx.get_height() / Image.Decor[1].get_height())-2):
            Image.Decor.draw(sheet, 1, Tool.stepoff(Image.Decor[0].get_size(), (x, y), 0, i+1))   
        
        for i in range(int(self.Menu_Frame.gfx.get_width() / Image.Decor[1].get_width())-2):
            Image.Decor.draw(sheet, 1, Tool.stepoff(Image.Decor[0].get_size(), (x, yy-Image.Decor[1].get_height()), i+1, 0))  
        
        for i in range(int(self.Menu_Frame.gfx.get_height() / Image.Decor[1].get_height())-2):
            Image.Decor.draw(sheet, 1, Tool.stepoff(Image.Decor[0].get_size(), (xx-Image.Decor[1].get_width(), y), 0, i+1))  
        
        self.Buttons["Start"].draw(sheet)
        self.Buttons["Create"].draw(sheet)
        self.Buttons["Sound"].draw(sheet)
        self.Buttons["Exit"].draw(sheet)


class ControlBar(Director.Scene):
    def __init__(self, active=False):
        super(ControlBar, self).__init__(active)
        self.Buttons = dict()
        self.load()
        
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


class GameView(Director.Scene):
    def __init__(self, active=False):
        super(GameView, self).__init__(active)
        self.load()

    def load(self):
        self.viewport = pygame.Rect(16, 16, System.width-(16*16), System.height-(16*8))
        self.view_bounds = Tool.pyrect_extend(self.viewport, 16)
        print(self.viewport)
        print(self.view_bounds)

    def update(self):
        pass

    def handle_events(self, event):
        pass
    
    def draw(self, sheet):
        self.draw_frame(sheet)
        
    def draw_frame(self, sheet):
        x = self.view_bounds[0]
        y = self.view_bounds[1]
        xx = self.view_bounds[2]
        yy = self.view_bounds[3]

        Image.Decor.draw(sheet, 0, (x, y))
        Image.Decor.draw(sheet, 0, (xx-Image.Decor[0].get_width(), y))
        Image.Decor.draw(sheet, 0, (x, yy-Image.Decor[0].get_height()))
        Image.Decor.draw(sheet, 0, (xx-Image.Decor[0].get_width(), yy-Image.Decor[0].get_height()))

        for i in range(int(self.view_bounds.width / Image.Decor[1].get_width())-2):
            Image.Decor.draw(sheet, 1, Tool.stepoff(Image.Decor[0].get_size(), (x, y), i+1, 0))

        for i in range(int(self.view_bounds.height / Image.Decor[1].get_height())-2):
            Image.Decor.draw(sheet, 1, Tool.stepoff(Image.Decor[0].get_size(), (x, y), 0, i+1))   
        
        for i in range(int(self.view_bounds.width / Image.Decor[1].get_width())-2):
            Image.Decor.draw(sheet, 1, Tool.stepoff(Image.Decor[0].get_size(), (x, yy-Image.Decor[1].get_height()), i+1, 0))  
        
        for i in range(int(self.view_bounds.height / Image.Decor[1].get_height())-2):
            Image.Decor.draw(sheet, 1, Tool.stepoff(Image.Decor[0].get_size(), (xx-Image.Decor[1].get_width(), y), 0, i+1))  


CentralMenu = CentralMenu()
ControlBar = ControlBar()
GameView = GameView()
