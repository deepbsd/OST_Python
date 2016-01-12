#!/usr/bin/env python3

from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(height=275, width=275)
        self.pack()
        self.createWidgets()


    def createWidgets(self):

        frame1 = Frame(self)
        self.label1 = Label(frame1, text="Frame 1")
        self.label1.pack()
        frame1.pack(side=TOP)


        frame2 = Frame(self)
        self.label2 = Label(frame2, text="Frame 2")
        self.label2.pack()
        frame2.pack(side=TOP)

        frame3 = Frame(self)
        self.label3 = Label(frame3, text="Frame 3")
        self.label3.pack()
        frame3.pack(side=RIGHT)


root = Tk()
app = Application(master=root)
app.mainloop()
