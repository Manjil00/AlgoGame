from tkinter import *
import sqlite3
root = Tk()

# Adding Start

# Database sqLite3

conn = sqlite3.connect("Dodge.db")
c = conn.cursor()

c.execute(
    """ CREATE TABLE block(
                 username str,
                 email str,
                 password str,
                 score_results int
    )"""
)


conn.commit()
conn.close()











mainloop()
