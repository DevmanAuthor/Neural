import System
import pygame
import Image
import Tool
import UI


def load(self): 
    self.Menu_Frame = Image.Sprite("gfx/UI/menuback.png", (50, 50))
    self.Menu_Frame.scale(160, 240)
    self.Menu_Frame.set_pos(Tool.center(self.Menu_Frame.gfx.get_size(), System.screen.get_rect()))

    self.Buttons["Start"] = UI.Button()
    self.Buttons["Start"].set_text("Embark", pygame.font.Font("font/homespun.ttf", 15))
    self.Buttons["Start"].set_pos(Tool.stepoffcenter(self.Buttons["Start"].currentsize, self.Menu_Frame.rect, 0, -2))

    self.Buttons["Sound"] = UI.ToggleButton(True, 0, 0, "gfx/UI/sound_on.png")
    self.Buttons["Sound"].scale(20, 20, True, 1.2, 1.2)
    self.Buttons["Sound"].set_pos(Tool.stepoffcenter(self.Buttons["Sound"].currentsize, self.Menu_Frame.rect, -2, 4))

    self.Buttons["Exit"] = UI.Button(0, 0, "gfx/UI/eyexit.png")
    self.Buttons["Exit"].scale(20, 20, True, 1.2, 1.2)
    self.Buttons["Exit"].set_pos(Tool.stepoffcenter(self.Buttons["Sound"].currentsize, self.Menu_Frame.rect, 2, 4))


def handle_events(self, event):
    retval = []
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
    self.Buttons["Sound"].draw(sheet)
    self.Buttons["Exit"].draw(sheet)
    pygame.draw.rect(sheet, System.RED, self.Menu_Frame.rect, 2)