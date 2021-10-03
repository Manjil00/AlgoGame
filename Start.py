from tkinter import *

root = Tk()
root.geometry("1280x720")
root.resizable(False, False)


def dashboard():
    global startButton_img
    start_game = LabelFrame(root).place(x=0, y=0)

    startbg_img = PhotoImage(file="Images/f1.png")
    startbg = Label(root, image=startbg_img).place(x=0, y=0)

    startButton_img = PhotoImage(file="Images/StartButton.png")
    startButton = Button(root, image=startButton_img,
                         bg="#000000",fg="#000000",
                         activebackground="#000000",
                         relief=FLAT,
                         bd=0,
                         )
    startButton.place(x=600, y=500)

dashboard()
root.mainloop()
