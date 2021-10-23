from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from random import randint
import sqlite3


attempt = 0


def window():
    def create_delete():
        root.destroy()
        window()

    def add_btn():
        btn2 = ttk.Button(frame1, text="თავიდან დაწყება !", command=create_delete)
        btn2.grid(row=4, columnspan=2)

    def answer():
        global attempt
        n = num.get()
        y = int(entry2.get())
        if n == y:
            attempt += 1
            labfornum["text"] = "Nice You Found Conceived Number !"
            label2["text"] = "Attempts: " + str(attempt)
            attempt = 0
            add_btn()
        elif n < y:
            attempt += 1
            labfornum["text"] = "Nice Try But Conceived Number is Higher !"
        elif n > y:
            attempt += 1
            labfornum["text"] = "Nice Try But Conceived Number is Lower !"

    root = Tk()
    root.geometry("400x375+525+240")
    root.title("Guess Number")

    num = IntVar()

    frame1 = ttk.Frame(root)
    frame1.pack()
    rand = randint(1, 5)

    label1 = Label(frame1, text="შეიტანეთ ციფრი 1-დან 100-მდე !")
    label1.grid(row=1, columnspan=2)

    label2 = Label(frame1, fg="Red")
    label2.grid(row=0, columnspan=2)

    entry1 = ttk.Entry(frame1, width=5, textvariable=num)
    entry1.grid(row=2, columnspan=2)

    entry2 = ttk.Entry(frame1)
    entry2.insert(0, rand)

    labfornum = Label(frame1)
    labfornum.grid(row=5, columnspan=2)

    btn1 = ttk.Button(frame1, text="პასუხის დადასტურება", command=answer)
    btn1.grid(row=3, columnspan=2)

    root.mainloop()


window()
