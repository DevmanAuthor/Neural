import os
import sys
import wx
import pygame


class Frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(350, 250))
        pygame.init()
        self.panel = wx.Panel(self)
        self.CreateStatusBar()
        self.display = pygame.display.set_mode((640, 480))
        self.display.fill((100, 100, 100))
        pygame.display.flip()
        filemenu = wx.Menu()
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)
        pos = wx.Point(10, 10)
        Open_Button = wx.Button(self, wx.ID_OPEN, "Open World", pos)
        Open_Button.Bind(wx.EVT_BUTTON, self.load, Open_Button)
        self.Show(True)
    
    def load(file, e):
        fh = open("Hello.txt", "a")
        fh.write("Hello")
        print(fh)
        return fh
        

app = wx.App(False)
frm = Frame(None, "Neural World Editor")
app.MainLoop()
       