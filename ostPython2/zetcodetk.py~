#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial
Jan Bodnar  www.zetcode.com
Jan 2011
Python 2.7 based
"""

from tkinter import *

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")

        self.parent = parent
        self.parent.title("Centered Window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):
        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))



def main():

    root = Tk()
    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()


