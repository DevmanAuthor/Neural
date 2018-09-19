import Director
import System
import Tool
import UI
import os
import pygame


class Editor(Director.Scene):
    def __init__(self, active):
        super(Editor, self).__init__(active)

        self.Button_New = UI.ToggleButton(False, 10, 10, None, "Open") 
        self.file_location = UI.TextBox("./stuff", pos=(70, 16))
        self.Background = Tool.load_image("gfx/UI/MenuBackground.png")
        self.view = pygame.Rect(64, 48, 640-(32*4), 480-(32*4))
        self.tilesize = 32
        self.bg = pygame.Surface(self.view.size)
        self.bg.fill(System.BLACK, self.view)
        self.poses = self.set_up_poses()
        
    def handle_events(self, event):
        self.file_location.handle_events(event)
        if "on" in self.Button_New.handle_events(event):
            mapdata = open(self.file_location.str, "w+")

    def draw(self, sheet):
        sheet.blit(self.Background, (0, 0))
        sheet.blit(self.bg, self.view.topleft)
        self.Button_New.draw(sheet)
        self.file_location.draw(sheet)
        if self.Button_New.Toggle is True:
            self.draw_grid(sheet)

    def set_up_poses(self):
        poses = list()
        for i in range(0, int(self.view[2] / self.tilesize)):
            for j in range(0, int(self.view[3] / self.tilesize)):
                poses.append((self.view[0]+(self.tilesize*i), self.view[1]+(self.tilesize*j)))
        print(poses)
        return poses

    def draw_grid(self, sheet):
        for i in self.poses:
            sheet.set_at(i, System.RED)
            rect = (i[0], i[1], self.tilesize, self.tilesize)
            pygame.draw.rect(sheet, System.GRAY, rect, 1)
            pygame.draw.rect(sheet, System.GREEN, self.view, 1)


ed = Editor(True)
List = [ed]
SceneManager = Director.SceneManager(List)


def Run():
    System.screen.fill(System.BLACK)
    while SceneManager is not None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                System.Quit()
            SceneManager.handle_events(event)
        System.time = System.checktime()
        SceneManager.check_active()
        SceneManager.update()
        pygame.transform.scale2x(System.render_sheet, System.screen)
        SceneManager.draw(System.screen)
        pygame.display.flip()


Run()