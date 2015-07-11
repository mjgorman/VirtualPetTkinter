#!/usr/bin/pythonw

from Tkinter import *
from ttk import Frame, Button, Style


class Start(Frame):
  def __init__(self, parent):
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

  def initBase(self):
    w = 320
    h = 240
    sw = self.parent.winfo_screenwidth()
    sh = self.parent.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
    self.style = Style()
    self.style.theme_use("default")
    self.columnconfigure(1, weight=1)
    self.columnconfigure(2, pad=7)
    self.columnconfigure(3, pad=7)
    self.rowconfigure(1, weight=1)
    self.rowconfigure(2, pad=7)

  def initLogo(self):
    logo = Text(self)
    logo.grid(row=1, column=1, columnspan=3)
    
  def initInterface(self):
    startButton = Button(self, text="Start", command=self.quit)
    startButton.grid(row=2, column=2)
    quitButton = Button(self, text="Quit", command=self.quit)
    quitButton.grid(row=2, column=3)
    
  def initUI(self):
    self.initMenu()
    self.initBase()
    self.initLogo()
    self.initInterface()

def main():
  root = Tk()
  app = Start(root)
  root.mainloop() 

if __name__ == "__main__":
  main()
