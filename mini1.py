import os
from tkinter import *
from tkinter import messagebox

root5 = Tk()

username = StringVar()
password = StringVar()

photo = PhotoImage(file='login2.png')
label1 = Label(root5, image=photo)
label1.pack()


def LoginP():
    root5.geometry("1920x1080")
    frame = Frame(root5, width=1900, height=1000, bg="#780e39")
    frame3 = Frame(frame, width=900, height=450, bg="#a64dff")
    username1 = Label(frame3, text="Username", font="0 30", bg="#a64dff")
    username1.grid(row=0, column=1)
    username_entry = Entry(frame3, textvariable=username, font='0 30', bg="#a366ff")
    username_entry.grid(row=0, column=2)
    password1 = Label(frame3, text="Password ", font="0 30", bg="#a64dff")
    password1.grid(row=3, column=1)
    password_entry = Entry(frame3, textvariable=password, font="0 30", show='*', bg="#a366ff")
    password_entry.grid(row=3, column=2)
    submit = Button(frame3, text="Submit", command=Check, font="0 25", bg="#a64dff")
    submit.grid(row=5, column=1)
    photo2 = PhotoImage(file="login1.png")
    button = Button(frame3, command=q, bg="#a64dff", image=photo2)
    button.grid(row=5, column=2)
    frame3.place(x=400, y=300)
    frame.pack()


def Check():
    if (username.get() == str("")) and (password.get() == str("")):
        messagebox.showerror("error", "Please Input Username and password")
    elif (username.get() == str("admin")) and (password.get() == str("12345")):
        os.system('HomePage.py')
        root5.destroy()
    else:
        messagebox.showerror("error", "Incorrect Username or password")


def q():
    answer = messagebox.askquestion("Exit", "Do you really want to exit?")
    if answer == "yes":
        root5.quit()


root5.title("Supermarket System")
LoginP()
root5.mainloop()
