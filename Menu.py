import Tool
import UI
import pygame
import sys

Buttons = dict()
Background = Tool.load_image("gfx/UI/MenuBackground.png")


def Load(sheet): 
    Buttons["Start"] = UI.Button()
    Buttons["Start"].place((sheet.get_width()/2)-Buttons["Start"].rect.centerx, (sheet.get_height()/2)-Buttons["Start"].rect.centery)
    Buttons["Start"].set_text("Start")
    Buttons["Exit"] = UI.Button(0, 0, "gfx/UI/exit.png")
    Buttons["Exit"].scale(20, 20, True)
    Buttons["Exit"].place(sheet.get_width()-Buttons["Exit"].rect.width-1, 0)


def Update(event):
    Buttons["Start"].handle_events(event)
    
    if 'clicked' in Buttons["Start"].handle_events(event):
        Buttons["Start"].set_text("BOOOM")
    else:
        Buttons["Start"].set_text("Go")


def Draw(sheet):
    sheet.blit(Background, (0, 0))
    Buttons["Start"].draw(sheet)
    Buttons["Exit"].draw(sheet)
    # print(PlayButton.pos, PlayButton._rect)






