from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sys

root = Tk()


class LoginP:
    def __init__(self, master):
        master.geometry("1720x980+0+0")
        master.resizable(False, False)
        self.frame = Frame(master)
        self.label1 = Label(self.frame, text="Choose Login", bg="blue", width="300", height="2", font=("Calibre", 30)).pack()
        self.label2 = Label(self.frame, text="Please enter details below", bg="blue").pack()
        self.label3 = Label(self.frame, text="").pack()

        self.username_entry = Entry(self.frame, textvariable="username")
        self.username_entry.pack()

        self.password_entry = Entry(self.frame, textvariable="password", show='*')
        self.password_entry.pack()

        self.button = Button(self.frame, text="Login", height="2", width="30", command=ref)
        self.button.pack()
        self.frame.pack()


def ref():
    os.system('HomePage.py')
    root.destroy()


root.title("Account Login")
a = LoginP(root)
root.mainloop()
