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
game.geometry("1280x720")
game.resizable(False, False)
signup_frame = LabelFrame(game, ).place(x=0, y=0)
login_frame = LabelFrame(game).place(x=0, y=0)
start_game = LabelFrame(game).place(x=0, y=0)


def login():
    global usernameentry
    global loginbg, black_bg, userLabel_img, sLabel, bg, passwordLabel_img, supLabel, sinLabel,usernameentry1

    login_frame = LabelFrame(game).place(x=0, y=0)

    def signinclick():
        global usernameentry1
        L = LabelFrame(login_frame).place(x=0, y=0)
        valid1 = False
        valid2 = False
        conn = sqlite3.connect("Dodge.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM block""")
        k = c.fetchall()
        h = len(k)
        for i in range(0, h):
            g = k[i]
            if g[0] == usernameentry.get() and g[2] == passwordentry.get():
                valid1 = True

            if tnc_check.get() == 1:
                valid2 = True

        if valid1 is False and valid2 is True:
            l1 = Label(login_frame, text="Wrong Credentials ", bg="#000000", fg="#FFFFFF").place(x=862, y=382)



        elif valid1 is True and valid2 is False:
            l2 = Label(login_frame, text="Please agree to Terms and Conditions", bg="#000000", fg="#FFFFFF").place(
                x=858, y=289)

        elif valid1 is True and valid2 is True:
            dashboard()
            usernameentry1=usernameentry.get()
            print(usernameentry1)

    # Adding login backgrounds
    loginbg = PhotoImage(file="Images/f1.png")
    background = Label(login_frame, image=loginbg, bg="#000000").place(x=-134, y=-31)

    # adding user login bg
    black_bg = PhotoImage(file="Images/BlackLabelWterms.png")
    blackframe = Label(login_frame, image=black_bg, bd=0, ).place(x=761, y=49)

    # Adding Username Label
    userLabel_img = PhotoImage(file="Images/Userlabel.png")
    userLabel = Label(login_frame, image=userLabel_img, bg="#000000").place(x=790.5, y=60)

    # Adding Username Entry
    usernameentry = StringVar()
    usernameentry.set("Username")
    userEntry = Entry(login_frame,
                      text=usernameentry,
                      font=("Arial,50"),
                      bg="#C8D9DB",
                      bd=0, relief=FLAT).place(x=874, y=77)

    # Adding pw Label
    passwordLabel_img = PhotoImage(file="Images/pwLabel.png")
    pwLabel = Label(login_frame, image=passwordLabel_img, bg="#000000").place(x=800, y=158)

    # Password Entry
    passwordentry = StringVar()
    passwordentry.set("Password")
    userEntry = Entry(login_frame,
                      text=passwordentry,
                      font=("Arial,50"),
                      bg="#C8D9DB",
                      bd=0, relief=FLAT).place(x=883, y=180)

    # Adding terms and condition check box and text
    checkB = StringVar()
    checkbutton_check = Checkbutton(login_frame, variable=checkB,
                                    onvalue="ON",
                                    offvalue="OFF",
                                    bg="#000000",
                                    activebackground="#000000",
                                    bd=0, )
    checkbutton_check.deselect()
    checkbutton_check.place(x=802, y=264)

    # Adding Start Button
    supLabel = PhotoImage(file="Images/signup.png")
    SignupLabel = Button(login_frame, image=supLabel,
                         bg="#000000",
                         activebackground="#000000",
                         relief=FLAT,
                         bd=0, command=signup,
                         ).place(x=801, y=309)

    sinLabel = PhotoImage(file="Images/signin.png")
    SigninLabel = Button(login_frame, image=sinLabel,
                         bg="#000000",
                         activebackground="#000000",
                         relief=FLAT,
                         bd=0, command=signinclick,
                         ).place(x=1007, y=309)

    tnc_check = IntVar()
    Checkbutton(
        login_frame,
        bg="#000000",
        bd=0,
        width=1,
        height=1,
        activebackground="#000000",
        variable=tnc_check,
        onvalue=1,
        offvalue=0,
    ).place(x=802, y=264)


# Adding SIGNIN page
def signup():
    global signupbg, sgnup_userimg, sgnup_passwordimg, signup_blackframe, sgnup_emailimg, sgnup_Buttonimg
    global usernameentry, sgnup_userentry

    signup_frame = LabelFrame(game, ).place(x=0, y=0)

    signupbg = PhotoImage(file="Images/rolexf1.png")
    signupbackg = Label(signup_frame, image=signupbg, relief=FLAT, bd=0)
    signupbackg.place(x=-110, y=-100)

    # Adding blackframe
    signup_blackframe = PhotoImage(file="Images/Signup_Blackframe.png")
    sup_blackframe = Label(signup_frame, image=signup_blackframe, relief=FLAT, bd=0).place(x=682, y=50)

    # Adding user Label and entry
    sgnup_userimg = PhotoImage(file="Images/user_entry.png")
    sgnup_userLabel = Label(signup_frame, image=sgnup_userimg, relief=FLAT, bd=0, ).place(x=717, y=85)

    sgnup_userentry = StringVar()
    sgnup_userentry.set("Username")
    userEntry = Entry(signup_frame,
                      text=sgnup_userentry,
                      font=("Arial,50"),
                      bg="#C8D9DB",
                      bd=0, relief=FLAT).place(x=826, y=101)

    # Adding email Label and entry
    sgnup_emailimg = PhotoImage(file="Images/emailEntry.png")
    sgnup_emailLabel = Label(signup_frame, image=sgnup_emailimg, relief=FLAT, bd=0, ).place(x=717, y=196)

    sgnup_Emailentry = StringVar()
    sgnup_Emailentry.set("Email")
    emailentry = Entry(signup_frame,
                       text=sgnup_Emailentry,
                       font=("Arial,50"),
                       bg="#C8D9DB",
                       bd=0,
                       relief=FLAT).place(x=826, y=209)

    # Adding PW Label and entry
    sgnup_passwordimg = PhotoImage(file="Images/PWentry.png")
    sgnup_passwordLabel = Label(signup_frame, image=sgnup_passwordimg, relief=FLAT, bd=0).place(x=717, y=307)

    sgn_passwordentry = StringVar()
    sgn_passwordentry.set("Password")
    passwordentry = Entry(signup_frame,
                          text=sgn_passwordentry,
                          font=("Arial,50"),
                          bg="#C8D9DB",
                          bd=0,
                          relief=FLAT).place(x=818, y=317)

    def signupclick():
        global usernameentry, sgnup_userentry
        conn = sqlite3.connect("Dodge.db")
        c = conn.cursor()
        c.execute(
            'INSERT INTO block VALUES(:username, :email, :password, :score_results)',
            {
                "username": sgnup_userentry.get(),
                "email": sgnup_Emailentry.get(),
                "password": sgn_passwordentry.get(),
                "score_results": 0,
            },

        )
        conn.commit()
        conn.close()



        login()

        # Adding Signup Button

    sgnup_Buttonimg = PhotoImage(file="Images/signupButton.png")
    sgnup_Button = Button(signup_frame,
                          image=sgnup_Buttonimg,
                          relief=FLAT, bd=0, bg="#000000", command=signupclick,
                          activebackground="#000000")
    sgnup_Button.place(x=928, y=432)


def dashboard():
    global startButton_img, startbg_img
    start_game = LabelFrame(game).place(x=0, y=0)

    startbg_img = PhotoImage(file="Images/f1.png")
    startbg = Label(game, image=startbg_img).place(x=0, y=0)

    startButton_img = PhotoImage(file="Images/StartButton.png")
    startButton = Button(game, image=startButton_img,
                         bg="#F31714", fg="#000000",
                         activebackground="#000000",
                         relief=FLAT,
                         bd=0, command=start
                         )
    startButton.place(x=600, y=100)


def start():
    global usernameentry1
    # Initiate pygame

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
    carimg = pygame.image.load('images/player.png')

    # Boundaries
    west_b = 132
    east_b = 700

    # Database sqLite3

    conn = sqlite3.connect("Dodge.db")
    c = conn.cursor()
    """
        c.execute(
         CREATE TABLE  block(
                 username str,
                 email str,
                 password str,
                 score_results int
        )
    )
    conn.commit()
    conn.close()
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
        conn = sqlite3.connect("Dodge.db")
        c = conn.cursor()
        c.execute(f"""SELECT * FROM block WHERE username='{usernameentry1}'""")
        d = c.fetchall()
        e = d[0]
        text2 = font.render('High-Score: ' + str(e[3]), True, BLACK)
        dodged_result = dodged
        wn.blit(text, (0, 0))
        wn.blit(text2, (0, 10))

    def crash():
        global dodged_result, usernameentry1

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
        c.execute(f"""SELECT * FROM block WHERE username='{usernameentry1}'""")
        d=c.fetchall()
        f = d[0]
        e = f[3]
        if e<= dodged_result:
            e = dodged_result
        d_0 = f[0]
        d_1 = f[1]
        d_2 = f[2]
        d_3 = e

        conn.commit()
        c.execute(f"""DELETE FROM block WHERE username='{usernameentry1}'""")
        conn.commit()
        c.execute(
            'INSERT INTO block VALUES(:username, :email, :password, :score_results)',
            {
                "username": d_0,
                "email": d_1,
                "password": d_2,
                "score_results": d_3,
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


login()
mainloop()
