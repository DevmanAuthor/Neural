import System
import Tool
import UI
import Entity
import Director
import Creatures

Background = Tool.load_image("gfx/UI/MenuBackground.png")


class MainMenu(Director.Scene):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.Buttons = dict()
        self.Load()

    def Load(self): 
        self.Buttons["Start"] = UI.Button()
        self.Buttons["Start"].place((System.screen.get_width()/2)-self.Buttons["Start"].rect.centerx, (System.screen.get_height()/2)-self.Buttons["Start"].rect.centery)
        self.Buttons["Start"].set_text("Start")
        self.Buttons["Exit"] = UI.Button(0, 0, "gfx/UI/exit.png")
        self.Buttons["Exit"].scale(20, 20, True)
        self.Buttons["Exit"].place(System.screen.get_width()-self.Buttons["Exit"].rect.width-1, 0)

    def Handle_Events(self, event):
        if 'clicked' in self.Buttons["Start"].handle_events(event):
            self.Buttons["Start"].set_text("Go!!!!!")
            self.nextscene = Game_Scene()
        if 'clicked' in self.Buttons["Exit"].handle_events(event):
            Tool.Quit()
            
    def Draw(self, sheet):
        System.screen.blit(Background, (0, 0))
        self.Buttons["Start"].draw(sheet)
        self.Buttons["Exit"].draw(sheet)


class Game_Scene(Director.Scene):
    def __init__(self):
        super(Game_Scene, self).__init__()
        self.Buttons = dict()
        self.Load()

    def Load(self): 
        self.Buttons["Help"] = UI.Button(0, 0, "gfx/UI/help.png")
        self.Buttons["Help"].scale(20, 20, True)
        self.Buttons["Help"].place(System.screen.get_width()-(self.Buttons["Help"].rect.width*2), 0)

        self.Buttons["Exit"] = UI.Button(0, 0, "gfx/UI/exit.png")
        self.Buttons["Exit"].scale(20, 20, True)
        self.Buttons["Exit"].place(System.screen.get_width()-self.Buttons["Exit"].rect.width-1, 0)

    def Handle_Events(self, event):
        if 'clicked' in self.Buttons["Help"].handle_events(event):
            self.nextscene = MainMenu()
        if 'clicked' in self.Buttons["Exit"].handle_events(event):
            System.Quit()
            
    def Draw(self, sheet):
        System.screen.blit(Background, (0, 0))
        self.Buttons["Help"].draw(sheet)
        self.Buttons["Exit"].draw(sheet)
