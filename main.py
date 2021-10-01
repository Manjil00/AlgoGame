"""Importing useful modules/ Libraries"""
import sqlite3
from tkinter import *
import pygame
import random
import math
from pygame import mixer
import os
import time

# from PIL import ImageTk, Image

game = Tk()
game.title = "F1 Road Block Launcher"
game.iconbitmap = ""
game.geometry("1280x720")
game.resizable(False, False)


def front():
    global loginbg, black_bg, userLabel_img, sLabel, bg, passwordLabel_img, supLabel, sinLabel

    front_frame = LabelFrame(game).pack()

    # Adding login backgrounds
    loginbg = PhotoImage(file="Images/f1.png")
    background = Label(front_frame, image=loginbg, bg="#000000").place(x=-134, y=-31)

    # adding user login bg
    black_bg = PhotoImage(file="Images/BlackLabelWterms.png")
    blackframe = Label(front_frame, image=black_bg, bd=0, ).place(x=761, y=49)



    # Adding Username Label
    userLabel_img = PhotoImage(file="Images/Userlabel.png")
    userLabel = Label(front_frame, image=userLabel_img, bg="#000000").place(x=790.5, y=60)

    # Adding Username Entry
    usernameentry=StringVar()
    usernameentry.set("Username")
    userEntry = Entry(front_frame,
                      text= usernameentry,
                      font=("Arial,50"),
                      bg="#C8D9DB",
                      bd=0,relief=FLAT).place(x=874, y=77)

    # Adding pw Label
    passwordLabel_img = PhotoImage(file="Images/pwLabel.png")
    pwLabel = Label(front_frame, image=passwordLabel_img, bg="#000000").place(x=800, y=158)

    #Password Entry
    passwordentry=StringVar()
    passwordentry.set("Password")
    userEntry = Entry(front_frame,
                      text=passwordentry,
                      font=("Arial,50"),
                      bg="#C8D9DB",
                      bd=0, relief=FLAT).place(x=883, y=180)

    # Adding terms and condition check box and text
    checkB = StringVar()
    checkbutton_check = Checkbutton(front_frame, variable=checkB,
                                    onvalue="ON",
                                    offvalue="OFF",
                                    bg="#000000",
                                    activebackground="#000000",
                                    bd=0,)
    checkbutton_check.deselect()
    checkbutton_check.place(x=802, y=264)

    # Adding Start Button
    supLabel = PhotoImage(file="Images/signup.png")
    SignupLabel = Button(front_frame, image=supLabel,
                         bg="#000000",
                         activebackground="#000000",
                         relief=FLAT,
                         bd=0,
                         ).place(x=801, y=309)

    sinLabel = PhotoImage(file="Images/signin.png")
    SigninLabel = Button(front_frame, image=sinLabel,
                         bg="#000000",
                         activebackground="#000000",
                         relief=FLAT,
                         bd=0,
                         ).place(x=1007, y=309)

    # Adding SIGNIN page

    def signup():
        global signupbg
        signup = LabelFrame(game).pack()

        # adding signupbg
        signupbg = PhotoImage(file="Images/rolexf1.png")
        signupbackg = Label(signup, image=signupbg, relief=FLAT, bd=0).place(x=0, y=0)

    def start():
        # Initiate pygame. Always needed

        pygame.init()

        # Clock
        clock = pygame.time.Clock()

        # RGB Color
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)

        # window with size of 500 x 400 pixels
        wn_width = 800
        wn_height = 600
        wn = pygame.display.set_mode((wn_width, wn_height))
        pygame.display.set_caption('F1 Road Block')

        # image
        bg = pygame.image.load('images/road.png')
        carimg = pygame.image.load('images/F1.png')

        # Boundaries
        west_b = 132
        east_b = 700

        # Database sqLite3
        """
        conn = sqlite3.connect("Dodge.db")
        c = conn.cursor()

        c.execute(
                 CREATE TABLE IF NOT EXISTS block(
                     score_results int,
               )
        )
        #conn.commit()
        #conn.close()
        """

        class Block:
            def __init__(self, x, y, width, height):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.speedy = 5
                self.dodged = 0

            def update(self):
                self.y = self.y + self.speedy
                # check boundary (block)
                if self.y > wn_height:
                    self.y = 0 - self.height
                    self.x = random.randrange(west_b, east_b - self.width)
                    self.dodged = self.dodged + 1

            def draw(self, wn):
                pygame.draw.rect(wn, RED, [self.x, self.y, self.width, self.height])

        class Player:
            def __init__(self):
                self.image = carimg
                self.width = self.image.get_width()
                self.height = self.image.get_height()

                self.rect = self.image.get_rect()
                self.rect.x = int(wn_width * 0.5)
                self.rect.y = int(wn_height * 0.5)

                self.speedx = 0

            def update(self):
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_LEFT]:
                    self.speedx = -10
                if keystate[pygame.K_RIGHT]:
                    self.speedx = 10

                self.rect.x = self.rect.x + self.speedx

                # check boundary (west)
                if self.rect.left < west_b:
                    self.rect.left = west_b
                # check boundary (east)
                if self.rect.right > east_b:
                    self.rect.right = east_b

        # Functions
        def score_board(dodged):
            global dodged_result

            font = pygame.font.Font(None, 25)
            text = font.render('Dodged: ' + str(dodged), True, BLACK)
            dodged_result = dodged
            wn.blit(text, (0, 0))

        def crash():
            global dodged_result
            font = pygame.font.Font(None, 80)
            text = font.render('YOU CRASHED!', True, BLACK)
            text_width = text.get_width()
            text_height = text.get_height()
            x = int(wn_width / 2 - text_width / 2)
            y = int(wn_height / 2 - text_height / 2)
            wn.blit(text, (x, y))
            pygame.display.update()
            time.sleep(2)

            conn = sqlite3.connect("Dodge.db")
            c = conn.cursor()
            c.execute(
                "INSERT INTO block VALUES (:score_results)",
                {
                    "score_results": dodged_result
                },
            )

            conn.commit()
            conn.close()

        # def game function
        def game_loop():

            block_width = 80
            block_height = 20
            block_x = random.randrange(west_b, east_b - block_width)
            block_y = -100

            player = Player()
            block = Block(block_x, block_y, block_width, block_height)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                player.update()
                block.update()

                wn.blit(bg, (0, 0))  # (0,0)location on the wn
                wn.blit(player.image, (player.rect.x, player.rect.y))
                block.draw(wn)

                # Car collision with block
                if player.rect.right > block.x and player.rect.x < block.x + block.width:
                    if block.y + block.height > player.rect.y and block.y < player.rect.bottom:
                        crash()

                # Score
                score_board(block.dodged)
                pygame.display.update()

                clock.tick(60)

            # pygame.quit

        game_loop()
        pygame.quit()
        quit()


front()
mainloop()
