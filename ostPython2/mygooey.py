#!/usr/bin/env python3

from tkinter import *

class MyApp:
    def __init__(self, parent):
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1, text="BUTT 1", bg="green")
        self.button1.pack(side=LEFT)

        self.button2 = Button(self.myContainer1)
        self.button2.configure(text="BUTT 2", bg="tan")
        self.button2.pack(side=LEFT)

        self.button3 = Button(self.myContainer1)
        self.button3.configure(text="BUTT 3", bg="cyan")
        self.button3.pack(side=LEFT)

        self.button4 = Button(self.myContainer1, text="BUTT 4", bg="red")
        self.button4.pack(side=LEFT)


dave = Tk()
app = MyApp(dave)
dave.mainloop()
