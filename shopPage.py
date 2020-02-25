from tkinter import *
from tkinter import messagebox
import os
import sys


root1 = Tk()


class ShopP:
    def __init__(self, master):
        master.geometry("1920x1080")
        self.frame = Frame(master, width=1920, height=1080, bg="#a64dff")

        self.canvas = Canvas(self.frame, width=200, height=159)
        self.canvas.place(x=0, y=0)
        self.photo1 = PhotoImage(file="shop.png")
        self.canvas.create_image(0, 0, image=self.photo1, anchor=NW)

        self.label1 = Label(self.frame, text="A's Supermarket", font="0 40 bold")
        self.label1.place(x=550, y=60)

        self.frame2 = Frame(self.frame)
        self.frame2.place(x=0, y=190)
        self.button1 = Button(self.frame2, font="30", text="Home", command=ref)
        self.button2 = Button(self.frame2, font="30", text="Shop")
        self.button3 = Button(self.frame2, font="30", text="bill", command=ref1)
        self.photo2 = PhotoImage(file="exit.png")
        self.button4 = Button(self.frame2, image=self.photo2, font="30", command=qu)
        self.button1.pack(side=LEFT, padx=160)
        self.button2.pack(side=LEFT, padx=160)
        self.button3.pack(side=LEFT, padx=160)
        self.button4.pack(side=RIGHT, padx=180)
        # self.frame3 = Frame(master, bg="red", width=700, height=400)
        # self.frame3.place(x=400, y=300)
        self.frame.pack()


def qu():
    answer = messagebox.askquestion("Exit", "Do you really want to exit?")
    if answer == "yes":
        root1.quit()


def donothing():
    pass


def ref():
    os.system('HomePage.py')
    root1.destroy()


def ref1():
    os.system('BillPage.py')
    root1.destroy()


root1.title("Supermarket System")
root1.protocol('WM_DELETE_WINDOW', donothing)
f = ShopP(root1)
root1.mainloop()
