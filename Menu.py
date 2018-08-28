import Tool
import UI
import pygbutton
import pygame

PlayButton = pygbutton.PygButton((100, 100, 0, 0), "Play")
Background = Tool.load_image("gfx/UI/MenuBackground.png")


def Load():
    PlayButton.setSurfaces("gfx/UI/BtnElevated.png", "gfx/UI/BtnPressed.png")

    

def Update(event):
    PlayButton.handleEvent(event)


def draw(sheet):
    sheet.blit(Background, (0, 0))
    PlayButton.draw(sheet)
    pygame.draw.rect(sheet, (225, 0, 0), GoButton._rect)


