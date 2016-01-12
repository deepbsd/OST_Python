#!/usr/bin/env python3

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(height=275, width=275)
        #create a menu bar
        menu = Menu(root)
        root.config(menu=menu)

        filemenu = Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.callback1)
        filemenu.add_command(label="Open...", command=self.callback2)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.callback3)

        helpmenu = Menu(menu, tearoff=False)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.callback4)

        self.cmenu = Menu(self, tearoff=False)
        self.cmenu.add_command(label="Copy", command=self.copy)
        self.cmenu.add_command(label="Paste", command=self.paste)
        self.bind("<Button-3>", self.popup)

        self.pack()
    

    def callback1(self):
        print("You selected 'File | New'")

    def callback2(self):
        print("You selected 'File |Open...'")

    def callback3(self):
        print("You selected 'File | Exit'")
        self.quit()

    def callback4(self):
        print("You selected 'Help | About...'")

    def copy(self):
        print("Context command 'Copy' selected")

    def paste(self):
        print("Context command 'Paste' selected")

    def popup(self, event):
        self.cmenu.post(event.x_root, event.y_root)


root = Tk()
app = Application(master=root)
app.mainloop()



