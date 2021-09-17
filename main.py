from tkinter import *

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
login_bg = PhotoImage(file="Images/LoginFrameBG.png")
loginframe = Label(game, image=login_bg, bd=0).place(x=761, y=49)

# Adding Username Label
userLabel_img = PhotoImage(file="Images/Userlabel.png")
userLabel = Label(game, image=userLabel_img, bg="#000000").place(x=790.5, y=79.5)

# Adding terms and condition check box and text

Label(game, text="I accept and understand all terms and conditions ",
            font=("Arial,8"),
            bd=0,
            bg="#FFFFFF").place(x=815, y=150)

"""
def start():
     Importing   
    import pygame
    import random
    import math
    from pygame import mixer
    import os
    import time

    #Loading Images

    playercar = pygame.image.load("Redcar.png"))
    enemycar = pygame.image.load(os.path.join("Images", "FireTruck.png"))

"""

mainloop()
