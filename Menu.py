import Tool
import UI
import pygame

Buttons = (UI.Button(100, 70), UI.Button(30, 200))
Background = Tool.load_image("gfx/UI/MenuBackground.png")


def Load(): 
    Buttons[0].scale(50, 50, True)
    Buttons[0].set_text("Stuff")
    pass


def Update(event):
    print(Buttons[0].rect)
    if 'clicked' in Buttons[0].handle_events(event):
        Buttons[0].move(10, 10)
    Buttons[1].handle_events(event)


def Draw(sheet):
    sheet.blit(Background, (0, 0))
    Buttons[0].draw(sheet)
    Buttons[1].draw(sheet)
    pygame.draw.rect(sheet, (225, 0, 0), Buttons[0].rect, 1)
    pygame.draw.rect(sheet, (225, 0, 0), Buttons[1].rect, 1)
    # print(PlayButton.pos, PlayButton._rect)






