import os
from tkinter import *
from tkinter import messagebox

root = Tk()


class HomeP:
    def __init__(self, master):
        master.geometry("1920x1080")
        # master.resizable(False, False)
        self.frame = Frame(master, width=1920, height=1080, bg="#a64dff")
        self.canvas = Canvas(self.frame, width=200, height=159, bg="#a64dff")
        self.canvas.place(x=0, y=0)
        self.photo1 = PhotoImage(file="home2.png")
        self.canvas.create_image(0, 0, image=self.photo1, anchor=NW)

        self.label1 = Label(self.frame, text="A's Supermarket", font="0 40 bold", bg="#a64dff")
        self.label1.place(x=550, y=60)

        self.frame2 = Frame(self.frame, bg="#9933ff", width=1080)
        self.frame2.place(x=0, y=190)
        self.button1 = Button(self.frame2, font="30", text="Home", bg="#a64dff")
        self.button2 = Button(self.frame2, font="30", text="Shop", bg="#a64dff", command=ref)
        self.button3 = Button(self.frame2, font="30", text="bill", bg="#a64dff")
        self.photo2 = PhotoImage(file="exit.png")
        self.button4 = Button(self.frame2, text="Quit", image=self.photo2, font="30", command=q, bg="#a64dff")
        self.button1.pack(side=LEFT, padx=160)
        self.button2.pack(side=LEFT, padx=160)
        self.button3.pack(side=LEFT, padx=160)
        self.button4.pack(side=RIGHT, padx=180)
        self.frame3 = Frame(master, width=700, height=400)
        self.photo3 = PhotoImage(file="background.png")
        self.label2 = Label(self.frame3, image=self.photo3).pack()
        self.frame3.place(x=350, y=270)
        self.frame.pack()


def q():
    answer = messagebox.askquestion("Exit", "Do you really want to exit?")
    if answer == "yes":
        root.quit()


def ref():
    os.system('shopPage.py')
    root.destroy()


def donothing():
    pass


root.protocol('WM_DELETE_WINDOW', donothing)
b = HomeP(root)
root.title("Supermarket System")
# root.resizable(0, 0)
root.mainloop()
