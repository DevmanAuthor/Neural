import Tool
import UI
import pygame

PlayButton = UI.Button(100, 70)
Background = Tool.load_image("gfx/UI/MenuBackground.png")


def Load(): 
    pass


def Update(event):
    print(PlayButton._rect)
    print(PlayButton.handle_events(event))


def Draw(sheet):
    sheet.blit(Background, (0, 0))
    PlayButton.draw(sheet)

    # pygame.draw.rect(sheet, (225, 0, 0), PlayButton._rect)
    # print(PlayButton.pos, PlayButton._rect)






