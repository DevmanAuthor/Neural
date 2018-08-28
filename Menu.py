import Tool
import UI
import pygame

PlayButton = UI.Button((100, 100, 0, 0), "Play")
Background = Tool.load_image("gfx/UI/MenuBackground.png")


def Load():
    PlayButton.setSurfaces("gfx/UI/BtnElevated.png", "gfx/UI/BtnPressed.png")


def Update(event):
    Btnev = PlayButton.handleEvent(event)
    if 'click' in Btnev:
        PlayButton.move((10, 10))
        print(PlayButton.pos)


def draw(sheet):
    sheet.blit(Background, (0, 0))
    PlayButton.draw(sheet)
    # pygame.draw.rect(sheet, (225, 0, 0), PlayButton._rect)
    # print(PlayButton.pos, PlayButton._rect)




