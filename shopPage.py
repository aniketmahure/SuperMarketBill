import mysql.connector
import mysql
from tkinter import *
from tkinter import messagebox
import os

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Shop")

root1 = Tk()
root1.overrideredirect(True)
root1.geometry("{0}x{0}+0+0".format(root1.winfo_screenwidth(), root1.winfo_screenheight()))
root1.resizable(False, False)
root1.configure(background="black")
en1 = StringVar()
en2 = StringVar()
en3 = StringVar()
en4 = StringVar()
en5 = StringVar()


class ShopP:
    def __init__(self, master):
        global x
        self.frame1 = Frame(master, width=1520, height=1080, bg="#a64dff")
        self.frame1.pack()

        self.file = PhotoImage(file="loginback.png")
        self.filename = Label(self.frame1, image=self.file)
        self.filename.place(x=0, y=0, relheight=1, relwidth=1)

        self.canvas = Canvas(self.frame1, width=200, height=159)
        self.canvas.place(x=0, y=0)
        self.photo1 = PhotoImage(file="shop.png")
        self.canvas.create_image(0, 0, image=self.photo1, anchor=NW)
        self.label1 = Label(self.frame1, text="A's Supermarket", font="Consolas 40 bold", bg="#68d2ce")
        self.label1.place(x=550, y=60)

        self.frame2 = Frame(self.frame1)
        self.frame2.place(x=0, y=190)
        self.pic = PhotoImage(file="new.png")
        self.menu = Label(self.frame2, image=self.pic)
        self.menu.place(x=0, y=0, relheight=1)
        self.button1 = Button(self.frame2, font="30", text="Home", bg="#7ccad0", command=self.ref, width=5)
        self.button2 = Label(self.frame2, font="30", text="Shop", bg="#7ccad0")
        self.button3 = Button(self.frame2, font="30", bg="#7ccad0", text="bill", command=self.ref1, width=5)
        self.photo2 = PhotoImage(file="exit.png")
        self.button4 = Button(self.frame2, image=self.photo2, font="30", command=self.qu)
        self.button1.pack(side=LEFT, padx=160)
        self.button2.pack(side=LEFT, padx=160)
        self.button3.pack(side=LEFT, padx=160)
        self.button4.pack(side=RIGHT, padx=180)

        self.button6 = Button(self.frame1, text="Refresh",bg="#7ccad0", font="0 14", command=self.Refresh)
        self.button6.place(x=740, y=255)

        self.frame3 = Frame(self.frame1, width=1520, height=470)
        self.pic2 = PhotoImage(file="snew.png")
        self.label7 = Label(self.frame3, image=self.pic2)
        self.label7.place(x=0, y=0, relheight=1, relwidth=1)
        self.frame3.place(x=0, y=300)
        self.button7 = Button(self.frame3, text="Delete", bg="#7ccad0", command=self.delete)
        self.button7.place(x=320, y=0)
        self.entry5 = Entry(self.frame3, textvar=en5, width=3, font="0 14")
        self.entry5.place(x=500, y=0)
        self.t = Text(self.frame3, font="0 25", width=37, bg="#f0f0f0")
        self.t.place(x=75, y=30)

        self.frame4 = Frame(self.frame3, width=600, height=470)
        self.frame4.place(x=840, y=30)
        self.label2 = Label(self.frame4, text="ID", font="0 14")
        self.label2.place(x=40, y=40)
        self.label6 = Label(self.frame4, textvariable=en1, width=3, font="0 14")
        self.label6.place(x=250, y=40)
        self.label3 = Label(self.frame4, text="Name", font="0 14")
        self.label3.place(x=40, y=90)
        self.entry1 = Entry(self.frame4, textvariable=en2, width=10, font="0 14")
        self.entry1.place(x=250, y=90)
        self.label4 = Label(self.frame4, text="Quantity", font="0 14")
        self.label4.place(x=40, y=150)
        self.entry2 = Entry(self.frame4, textvariable=en3, width=3, font="0 14")
        self.entry2.place(x=250, y=150)
        self.label5 = Label(self.frame4, text="Price", font="0 14")
        self.label5.place(x=40, y=210)
        self.entry3 = Entry(self.frame4, textvariable=en4, width=3, font="0 14")
        self.entry3.place(x=250, y=210)
        self.button5 = Button(self.frame4, text="Update", font="0 14", command=self.update)
        self.button5.place(x=280, y=320)

        mcursor = mydb.cursor()
        mcursor.execute("select Product_Name,Product_Quantity,Product_Price from items")
        myresult = mcursor.fetchall()
        x = 1
        for row in myresult:
            self.t.insert(END, row)
            self.t.insert(END, "rs/Q")
            self.t.insert(END, "\n")
        en1.set(self.count())

    def count(self):
        mcursor = mydb.cursor()
        mcursor.execute("select count(Product_id) from items")
        x = mcursor.fetchone()
        for y in x:
            x = y
        x = x + 1
        return x

    def update(self):
        m1cursor = mydb.cursor()
        if en4.get() != '' or en2.get() != '' or en3.get() != '':
            sql = "INSERT INTO items (Product_Id,Product_Name, Product_Quantity, Product_Price) VALUES (%s, %s, " \
                  "%s, %s) "
            val = (en1.get(), en2.get(), en3.get(), en4.get())
            m1cursor.execute(sql, val)
            mydb.commit()
        else:
            messagebox.showerror("error", "Please Input Valid ID")
        en1.set(self.count())
        en2.set("")
        en4.set("")
        en3.set("")

    def delete(self):
        m1cursor = mydb.cursor()
        b = (en5.get(),)
        m1cursor.execute("DELETE FROM items WHERE Product_Id = %s ", b)
        mydb.commit()
        en1.set(self.count())
        en5.set(self.count())

    def Refresh(self):
        self.t.delete(1.0, END)
        mcursor = mydb.cursor()
        mcursor.execute("select Product_Name,Product_Quantity,Product_Price from items")
        myresult = mcursor.fetchall()
        for column in myresult:
            self.t.insert(END, column)
            self.t.insert(END, "rs/Q")
            self.t.insert(END, "\n")

    def qu(self):
        answer = messagebox.askquestion("Exit", "Do you really want to exit?")
        if answer == "yes":
            root1.quit()

    def ref(self):
        root1.destroy()
        os.system('HomePage.py')

    def ref1(self):
        root1.destroy()
        os.system('BillPage.py')


def donothing():
    pass

root1.protocol('WM_DELETE_WINDOW', donothing)
f = ShopP(root1)
root1.wm_iconbitmap("Shop.ico")
root1.title("Supermarket System : ShopPage")
root1.mainloop()
