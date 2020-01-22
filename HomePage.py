from tkinter import *
from tkinter import messagebox

root = Tk()


class HomeP:
    def __init__(self, master):
        master.geometry("1920x1080")
        self.frame = Frame(master, width=1920, height=1080)

        self.canvas = Canvas(self.frame, width=200, height=159)
        self.canvas.place(x=0, y=0)
        self.photo1 = PhotoImage(file="home2.png")
        self.canvas.create_image(0, 0, image=self.photo1, anchor=NW)

        self.label1 = Label(self.frame, text="A's Supermarket", font="0 40 bold")
        self.label1.place(x=550, y=60)

        self.frame2 = Frame(self.frame)
        self.frame2.place(x=0, y=190)
        self.button1 = Button(self.frame2, font="30", text="Home")
        self.button2 = Button(self.frame2, font="30", text="Shop")
        self.button3 = Button(self.frame2, font="30", text="bill")
        self.button4 = Button(self.frame2, text="Quit", font="30", command=qu)
        self.button1.pack(side=LEFT, padx=150)
        self.button2.pack(side=LEFT, padx=150)
        self.button3.pack(side=LEFT, padx=150)
        self.button4.pack(side=RIGHT, padx=150)
        self.frame3 = Frame(master, bg="red", width=700, height=400)
        self.frame3.place(x=400, y=300)
        self.canvas1 = Canvas(self.frame3)
        self.canvas1.pack()
        self.photo2 = PhotoImage(file="home1.png")
        self.canvas1.create_image(0, 0, image=self.photo2, anchor=NW)

        self.frame.pack()


def qu():
    answer = messagebox.askquestion("Exit", "Do you really want to exit?")
    if answer == "yes":
        root.quit()


b = HomeP(root)
root.mainloop()

