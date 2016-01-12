#!/usr/bin/env python3


from tkinter import *


root = Tk()
root.title("Testing this stuff")

ALL = N+S+E+W

frame1 = Frame(root)

root.rowconfigure(0, weight=5)
root.columnconfigure(0, weight=5)
root.columnconfigure(1, weight=5)
frame1.rowconfigure(0, weight=5)
frame1.columnconfigure(0, weight=5)
frame1.columnconfigure(1, weight=5)

label_1 = Label(frame1, text="One")
label_1.config(bg="green", height=10, width=10)
label_2 = Label(frame1, text="Two")
label_2.config(bg="yellow", height=10, width=10)


label_1.grid(row=0, column=0, sticky=ALL)
label_2.grid(row=0, column=1, sticky=ALL)

frame1.grid(row=0, column=0, sticky=ALL)


root.mainloop()
