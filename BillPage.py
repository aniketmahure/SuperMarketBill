from tkinter import *
from tkinter import messagebox
import os
import sys


root2 = Tk()
root2.overrideredirect(True)
root2.geometry("{0}x{0}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
root2.resizable(False, False)
root2.configure(background="black")

qnt = IntVar()
s = StringVar()
Entry1 = StringVar()
Entry2 = StringVar()


class ShopP:
    def __init__(self, master):
        master.geometry("1920x1080")
        self.frame = Frame(master, width=1920, height=1080, bg="#a64dff")

        self.canvas = Canvas(self.frame, width=200, height=159, bg="#a64dff")
        self.canvas.place(x=0, y=0)
        self.photo1 = PhotoImage(file="buy.png")
        self.canvas.create_image(0, 0, image=self.photo1, anchor=NW)

        self.label1 = Label(self.frame, text="A's Supermarket", font="0 40 bold", bg="#a64dff")
        self.label1.place(x=550, y=60)

        self.frame2 = Frame(self.frame, bg="#9933ff")
        self.frame2.place(x=0, y=190)
        self.button1 = Button(self.frame2, font="0 15", text="Home", command=ref, bg="#a64dff")
        self.button2 = Button(self.frame2, font="0 15", text="Shop", command=ref1, bg="#a64dff")
        self.button3 = Label(self.frame2, font="0 15", text="Bill", bg="#9933ff")
        self.photo2 = PhotoImage(file="exit.png")
        self.button4 = Button(self.frame2, text="Quit", image=self.photo2, command=qu, bg="#a64dff")
        self.button1.pack(side=LEFT, padx=160)
        self.button2.pack(side=LEFT, padx=160)
        self.button3.pack(side=LEFT, padx=160)
        self.button4.pack(side=RIGHT, padx=180)
        self.frame4 = Frame(self.frame, bg="#a64dff", width=600, height=475)
        self.frame4.place(x=20, y=290)
        self.frame3 = Frame(self.frame, bg="white", width=825, height=475)
        self.frame3.place(x=600, y=290)
        self.Entry = Entry(self.frame4, textvariable=s).grid(row=0, column=0)
        s.set("Search")
        self.button5 = Button(self.frame4, text="search").grid(row=0, column=1)
        self.label2 = Label(self.frame4, text="Snacks").grid(row=1, column=0)
        self.label3 = Label(self.frame4, text="Drinks").grid(row=1, column=1)
        self.label4 = Label(self.frame4, text="Objects").grid(row=1, column=3)
        self.button6 = Button(self.frame4, text="+").grid(row=2, rowspan=1, column=4)
        self.Entry3 = Entry(self.frame4, width=4, textvariable=qnt).grid(row=2, column=5)
        self.button7 = Button(self.frame4, text="-").grid(row=2, column=6)
        self.button8 = Button(self.frame4, text="Add", command=self.add1).grid(row=3, column=4)
        self.button9 = Button(self.frame4, text="remove").grid(row=3, column=5)

        self.Lb1 = Listbox(self.frame4, selectmode=MULTIPLE)
        self.Lb1.insert(0, "Select")
        self.Lb1.insert(1, "Biscuits")
        self.Lb1.insert(2, "Soap")
        self.Lb1.insert(3, "Chips")
        self.Lb1.insert(4, "Shampoo")
        self.Lb1.insert(5, "Pen")
        self.Lb1.insert(6, "Brush")
        self.Lb1.insert(7, "BedSheet")
        self.Lb1.insert(8, "Maggie")
        self.Lb1.insert(9, "Bread")
        self.Lb1.insert(10, "Wafers")
        self.Lb1.insert(11, "Parle-G")
        self.Lb1.insert(12, "Chocolate")
        self.Lb1.grid(row=2, column=0)

        self.Lb2 = Listbox(self.frame4, selectmode=MULTIPLE)
        self.Lb2.insert(0, "Select")
        self.Lb2.insert(1, "Due")
        self.Lb2.insert(2, "Pepsi")
        self.Lb2.insert(3, "Sprite")
        self.Lb2.insert(4, "Slice")
        self.Lb2.insert(5, "Coca cola")
        self.Lb2.grid(row=2, column=1)

        self.Lb3 = Listbox(self.frame4, selectmode=MULTIPLE)
        self.Lb3.insert(1, "Select")
        self.Lb3.grid(row=2, column=3)

        self.label5 = Label(self.frame3, text="Customer Name").grid(row=0, column=0)
        self.Entry1 = Entry(self.frame3).grid(row=0, column=1)
        self.label6 = Label(self.frame3, text="Mobile No").grid(row=1, column=0)
        self.Entry2 = Entry(self.frame3).grid(row=1, column=1)
        self.label7 = Label(self.frame3, text="Selected Items").grid(row=2, columnspan=2)

        self.tx = Text(self.frame3, height=6, width=30, bd=1).grid(row=3, column=0)
        self.frame.pack()

    def add1(self):
        data = self.Lb1.get(ACTIVE)
        if data == 'Pen':
            self.tx.insert(END, '\nPen - %d' % (qnt.get() + 1))
            # List1.append(10 * (qnt.get() + 1))
        elif data == 'Pencil 5/-':
            self.tx.insert(END, '\nPencil - %d' % (qnt.get() + 1))
            # Lb1.append(5 * (qnt.get() + 1))
        elif data == 'Eraser 10/-':
            self.tx.insert(END, '\nEraser\t10/- x %d' % (qnt.get() + 1))
            # Lb1.append(10 * (qnt.get() + 1))
        elif data == 'Sharpner 15/-':
            self.tx.insert(END, '\nSharpner\t15/- x %d' % (qnt.get() + 1))
            # Lb1.append(15 * (qnt.get() + 1))
        elif data == 'Notebook 30/-':
            self.tx.insert(END, '\nNotebook\t30/- x %d' % (qnt.get() + 1))
            # Lb11.append(30 * (qnt.get() + 1))
        elif data == 'Scale 12/-':
            self.tx.insert(END, '\nScale\t12/- x %d' % (qnt.get() + 1))
            # Lb11.append(12 * (qnt.get() + 1))
        elif data == 'A4 paper 1/-':
            self.tx.insert(END, '\nA4 paper\t1/- x %d' % (qnt.get() + 1))
            self.Lb1.append(1 * (qnt.get() + 1))


def qu():
    answer = messagebox.askquestion("Exit", "Do you really want to exit?")
    if answer == "yes":
        root2.quit()


def donothing():
    pass


def ref():
    os.system('HomePage.py')
    root2.destroy()


def ref1():
    os.system('shopPage.py')
    root2.destroy()


root2.protocol('WM_DELETE_WINDOW', donothing)
f = ShopP(root2)
root2.wm_iconbitmap("Shop.ico")
root2.title("Supermarket System : BillPage")
root2.mainloop()
