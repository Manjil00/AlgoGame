from tkinter import*
game=Tk()
global signupbg
signup = LabelFrame(game).pack()

# adding signupbg
signupbg = PhotoImage(file="Images/rolexf1.png")
signupbackg = Label(signup, image=signupbg, relief=FLAT, bd=0).place(x=0, y=0)








mainloop()
