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

def main():
  root = Tk()
  app = Start(root)
  root.lift()
  root.call('wm', 'attributes', '.', '-topmost', True)
  root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)
  root.mainloop() 

if __name__ == "__main__":
  main()
