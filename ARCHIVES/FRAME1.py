#name of the frame1 is: FRAME1
#name of the frame2 is: FRAME2

from tkinter import *

class FRAME1class(Frame)
  def __init__(self, master=None):
    Frame.__init__(self, master)
    FRAME1 = Frame(master, bg="black")
    FRAME1.grid(row=0, column=0, padx=5, pady=5)
    
    FRAME2 = Frame(master)
    FRAME2.grid(row=0, column=1)
