from tkinter import*
game=Tk()

game.geometry("800x600")
game.resizable(False,False)
global signupbg
signup = LabelFrame(game).pack()

# Adding signupbg

signupbg = PhotoImage(file="Images/rolexf1.png")
signupbackg = Label(signup, image=signupbg, relief=FLAT, bd=0).place(x=-110, y=-100)

signup_blackframe=PhotoImage(file="Images/")
sup_blackframe=Label(signup,image=signup_blackframe,relief=FLAT,bd=0).place(x=,y=)








mainloop()
