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


def draw(screen):
    screen.blit(Background, (0, 0))
    PlayButton.draw(screen)
    # pygame.draw.rect(screen, (225, 0, 0), PlayButton.rect)


