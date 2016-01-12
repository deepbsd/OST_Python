#!/usr/bin/env python3

from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("Hi there, everyone!")

    def createWidgets(self):
        Button(self, text="Hello", fg="blue", command=self.say_hi).pack(side="left")

        Button(self, text="Goodbye", fg="red", command=self.quit).pack(side="left")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()


