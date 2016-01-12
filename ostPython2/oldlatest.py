#!/usr/local/bin/python3

#  OST Python2 Class, Lesson 4
#   File Handling, Jan 13, 2015
#   David S. Jackson for
#   Instructor Pat Barton
#
#    Code is copies from text...
#
import glob
import os

pathstem = "/home/dsj/bin/tmp/"

def latest(num=1, path="."):
    files = glob.glob(os.path.join(path, "*"))
    dated_files = [(os.path.getmtime(fn), os.path.abspath(fn)) for fn in files]
    dated_files.sort()
    latest_files = [f for (d, f) in dated_files[-num:]]
    latest_files.reverse()
    return latest_files

if __name__ == "__main__":
    print(latest(3, pathstem))

