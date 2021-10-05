from tkinter import *

root = Tk()
root.tile("mini")
data = StringVar()
qnt = IntVar()


class ShopP:
    def __init__(self, master):
        self.frame = Frame(master, width=1920, height=1080, bg="#a64dff")
        self.Lb = Listbox(self.frame, selectmode=MULTIPLE)
        self.Lb.insert(1, "Pen")
        self.Lb.insert(2, "Pencil")
        self.Lb.insert(3, "Paper")
        self.Lb.pack()
        self.Button3 = Button(self.frame, text="+", command=self.add1).pack()
        self.entry1 = Entry(self.frame, textvariable=qnt).pack()
        qnt.set(1)
        self.Button4 = Button(self.frame, text="-").pack()
        self.button1 = Button(self.frame, text="add", command=self.show).pack()
        self.button2 = Button(self.frame, text="remove").pack()
        self.tx = Text(self.frame, width=20, height=10).pack()
        self.frame.pack()

    def add1(self):
        if qnt.get() > str("0"):
            # qnt.get() = qnt.get() + 1
            print(qnt.get)

    def sub(self):
        self.qnt.get = self.qnt.get - 1

    def add(self):
     #   data = self.Lb.get(ACTIVE)
          data = self.Lb.get(ACTIVE)
    def show(self):
        items = self.Lb.curselection()
        self.tx.insert(INSERT, qnt.get())
        self.tx.get(1.0, END)
        print(self.Lb.get(items))


b = ShopP(root)
root.mainloop()
