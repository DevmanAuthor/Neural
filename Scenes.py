import System
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
        self.Buttons["Start"] = UI.Button(0, 0, None, "Start")
        self.Buttons["Start"].place((System.screen.get_width()/2)-self.Buttons["Start"].rect.centerx, (System.screen.get_height()/2)-self.Buttons["Start"].rect.centery)
        self.Buttons["Toggle"] = UI.ToggleButton(0, 0, None, "OFF")

    def Handle_Events(self, event):
        if "clicked" in self.Buttons["Start"].handle_events(event):
            self.Buttons["Start"].set_text("Soon to be Implemented")
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


'''
class Game_Scene(Director.Scene):
    def __init__(self):
        super(Game_Scene, self).__init__()
        self.Buttons = dict()
        self.Load()

    def Load(self): 
        self.Buttons["Help"] = UI.Button(0, 0, "gfx/UI/help.png")
        self.Buttons["Help"].scale(20, 20, True)
        self.Buttons["Help"].place(System.screen.get_width()-(self.Buttons["Help"].rect.width*2), 0)

        self.Buttons["Exit"] = UI.Button(0, 0, "gfx/UI/eyexit.png")
        self.Buttons["Exit"].scale(40, 40, True, 1.5, 1.5)
        self.Buttons["Exit"].place(System.screen.get_width()-(self.Buttons["Exit"].rect.width*3), System.screen.get_height()-(self.Buttons["Exit"].rect.height))

    def Handle_Events(self, event):
        if 'clicked' in self.Buttons["Help"].handle_events(event):
            self.nextscene = MainMenu()
        if 'clicked' in self.Buttons["Exit"].handle_events(event):
            System.Quit()
            
    def Draw(self, sheet):
        self.Buttons["Help"].draw(sheet)
        self.Buttons["Exit"].draw(sheet)
'''