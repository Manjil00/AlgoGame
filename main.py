"""Importing useful modules/ Libraries"""

from tkinter import *
import pygame
import random
import math
from pygame import mixer
import os
import time
# from PIL import ImageTk, Image

game = Tk()
game.title = "Drag Race"
game.iconbitmap = ""
game.geometry("1280x720")
game.resizable(False, False)

# Adding login backgrounds
bg = PhotoImage(file="Images/Loginbg.png")
background = Label(game, image=bg).place(x=0, y=0)

# adding user login bg
login_bg = PhotoImage(file="Images/LoginLabelwithTerms.png")
loginframe = Label(game, image=login_bg, bd=0).place(x=761, y=49)

username=StringVar()
userEntry=Entry(game,text="Username",
      font=("Arial,30"),
      bg="#000000",
      bd=0)
userEntry.place(x=860,y=102)

# Adding Username Label
userLabel_img = PhotoImage(file="Images/Userlabel.png")
userLabel = Label(game, image=userLabel_img, bg="#000000").place(x=790.5, y=60)

# Adding terms and condition check box and text
checkB=StringVar()
Checkbutton=Checkbutton(game,variable=checkB,
                        onvalue="ON",
                        offvalue="OFF",
                        bg="#000000",
                        activebackground="#000000",
                        bd=0,)
Checkbutton.deselect()
Checkbutton.place(x=802,y=143.38)



# Adding Start Button
sLabel = PhotoImage(file="Images/StartButton.png")
startLabel = Button(game, image=sLabel,
                    bg="#000000",
                    activebackground="#000000",
                    relief=FLAT,
                    bd=0,
                    ).place(x=953, y=190)

def start():





    mainloop()
