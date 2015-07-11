#!/usr/bin/python

from Tkinter import *
from ttk import Frame, Button, Style

class BaseTemplate(Frame):
  def __init__(self, parent, takefocus=1):
    Frame.__init__(self, parent)
    self.parent = parent
    self.parent.title("Starting")
    self.pack(fill=BOTH, expand=1)
    self.initUI()

  def initMenu(self):
    menubar = Menu(self.parent)
    self.parent.config(menu=menubar)
    fileMenu = Menu(menubar)
    fileMenu.add_command(label="Exit", command=self.quit)
    menubar.add_cascade(label="File", menu=fileMenu) 

  def initBase(self, w=640, h=480):
    sw = self.parent.winfo_screenwidth()
    sh = self.parent.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
    self.style = Style()
    self.style.theme_use("default")
    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, pad=7)
    self.columnconfigure(2, pad=7)
    self.rowconfigure(0, weight=1)
    self.rowconfigure(1, pad=7)

  def initInterface(self):
    startButton = Button(self, text="Start", command=self.quit)
    startButton.grid(row=1, column=1)
    quitButton = Button(self, text="Quit", command=self.quit)
    quitButton.grid(row=1, column=2)
    
  def initUI(self):
    self.initMenu()
    self.initBase()
    self.initInterface()
