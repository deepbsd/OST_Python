#!/usr/bin/env python3


from tkinter import *

root = Tk()
root.title("Hi Pat!")
ALL=N+S+E+W

frame1 = Frame(root)

for r in (0, 1):
    root.rowconfigure(r, weight=1)
    frame1.rowconfigure(r, weight=1)
    for c in (0, 1):
        root.columnconfigure(c, weight=1)
        frame1.columnconfigure(c, weight=1)

label_1 = Label(frame1, text="One")
label_1.config(bg="yellow", height=10, width=10)
label_2 = Label(frame1, text="Two")
label_2.config(bg="cyan", height=10, width=10)
label_3 = Label(frame1, text="Three")
label_3.config(bg="green", height=20, width=10)

label_1.grid(row=0, column=0, sticky=ALL)
label_2.grid(row=1, column=0, sticky=ALL)
label_3.grid(row=0, column=1, rowspan=2, columnspan=1, sticky=ALL)




frame1.grid(sticky=ALL)



root.mainloop()
