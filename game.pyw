#!/usr/bin/python

from Tkinter import *
import PIL
from PIL import ImageTk, Image
from ttk import Frame, Button, Style
from frames import BaseTemplate

class Start(BaseTemplate):
  def initLogo(self):
    logoimg = Image.open("logo.jpg")
    logotk = ImageTk.PhotoImage(logoimg)
    logo = Label(self, image=logotk, borderwidth=0, highlightthickness=0)
    logo.img = logotk
    logo.grid(row=0, column=0, columnspan=3)
    
  def initUI(self):
    self.initMenu()
    self.initBase(w=340, h=240)
    self.initLogo()
    self.initInterface()

  def load_started(self):
    self.parent.destroy()
    self.load_started = Started(Tk())


  def initInterface(self):
    startButton = Button(self, text="Start", command=self.load_started)
    startButton.grid(row=1, column=1)
    quitButton = Button(self, text="Quit", command=self.quit)
    quitButton.grid(row=1, column=2)

class Started(BaseTemplate):

  def initInterface(self):
    header = Label(self, text="Pet Status:")
    header.grid(sticky=NW, row=0, column=0)


def main():
  root = Tk()
  app = Start(root)
  root.lift()
  root.call('wm', 'attributes', '.', '-topmost', True)
  root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)
  root.mainloop() 

if __name__ == "__main__":
  main()
