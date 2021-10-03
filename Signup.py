from tkinter import *

game = Tk()

game.geometry("1280x720")
game.resizable(False, False)
global signupbg
signup = LabelFrame(game).pack()

# Adding signupbg
def signup():
    signupbg = PhotoImage(file="Images/rolexf1.png")
    signupbackg = Label(signup, image=signupbg, relief=FLAT, bd=0).place(x=-110, y=-100)

    # Adding blackframe
    signup_blackframe = PhotoImage(file="Images/Signup_Blackframe.png")
    sup_blackframe = Label(signup, image=signup_blackframe, relief=FLAT, bd=0).place(x=682, y=50)

    # Adding user Label and entry
    sgnup_userimg = PhotoImage(file="Images/user_entry.png")
    sgnup_userLabel = Label(signup, image=sgnup_userimg, relief=FLAT, bd=0, ).place(x=717, y=85)

    sgnup_userentry = StringVar()
    sgnup_userentry.set("Username")
    userEntry = Entry(signup,
                      text=sgnup_userentry,
                      font=("Arial,50"),
                      bg="#C8D9DB",
                      bd=0, relief=FLAT).place(x=826, y=101)

    # Adding email Label and entry
    sgnup_emailimg = PhotoImage(file="Images/emailEntry.png")
    sgnup_emailLabel = Label(signup, image=sgnup_emailimg, relief=FLAT, bd=0, ).place(x=717, y=196)

    sgnup_Emailentry = StringVar()
    sgnup_Emailentry.set("Email")
    emailentry = Entry(signup,
                       text=sgnup_Emailentry,
                       font=("Arial,50"),
                       bg= "#C8D9DB",
                       bd=0,
                       relief=FLAT).place(x=826,y=209)


    # Adding PW Label and entry
    sgnup_passwordimg = PhotoImage(file="Images/PWentry.png")
    sgnup_passwordLabel = Label(signup, image=sgnup_passwordimg, relief=FLAT, bd=0).place(x=717, y=307)

    sgn_passwordentry = StringVar()
    sgn_passwordentry.set("Password")
    passwordentry = Entry(signup,
                       text=sgn_passwordentry,
                       font=("Arial,50"),
                       bg= "#C8D9DB",
                       bd=0,
                       relief=FLAT).place(x=818,y=317)



    # Adding Signup Button
    sgnup_Buttonimg = PhotoImage(file="Images/signupButton.png")
    sgnup_Button = Button(signup,
                          image=sgnup_Buttonimg,
                          relief=FLAT, bd=0,bg="#000000",
                          activebackground="#000000").place(x=928, y=432)

signup()
mainloop()
