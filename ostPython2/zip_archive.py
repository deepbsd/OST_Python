#!/usr/bin/env python3
#
#
#             zip_archive.py
#
#     for OST Python2: Lesson 6 Archives
#
#     by David S Jackson on Feb 1, 2015
#
#          Instructor: Pat Barton
#
""" 
This project creates a zipfile containing only the zipped files and the
parent directory they are contained in (using os.path.basename()).  Only files
are contained in the zip archive.  No symlinks or directories or anything else
are contained in the archive.  The project further handles posix and Windows
path seperators ("/" vs "\") using os.path.normpath().  All paths recorded in
the zipfile should start with the base directory.  
"""


import os
import shutil
import zipfile
import glob

testdir = "/home/dsj/bin/testdir1"
#testdir = "v:\workspace\Archives_Homework\src\testdir1"
myzipfile = "testzip.zip"


def zipit(fn=myzipfile, dirpath=testdir):
    "This function creates the zipfile named fn of files in dirpath"
    zf = zipfile.ZipFile(fn, "w")
    dirpath = os.path.basename(dirpath)
    filenames = glob.glob(os.path.join(dirpath, "*"))
    #[zf.write(fn) for fn in filenames if os.path.isfile(fn)]
    for fn in filenames:
        if os.path.isfile(fn):
            os.path.normpath(fn)
            zf.write(fn)
    zf.close()


def mk_testfiles(fn=myzipfile, dirpath=testdir):
    "Makes three testfiles inside a testdirectory named dirpath"
    filenames = ['one', 'two', 'three']
    os.mkdir(dirpath)
    for fn in filenames:
        f = open(os.path.join(dirpath, fn), 'w')
        f.close()
    

def list_zipfile(fn=myzipfile):
    "lists contents of the zipfile named fn"
    zf = zipfile.ZipFile(fn)
    lst = zf.namelist()
    zf.close()
    print("Files in archive: ")
    for fn in sorted(lst):
        print(os.path.normpath(fn))


def rm_testfiles(fn=myzipfile, dirpath=testdir):
    "removes testfiles and test directory"
    shutil.rmtree(dirpath)
    os.remove(fn)
    


if __name__ == "__main__":
    mk_testfiles()
    zipit()
    list_zipfile()
    rm_testfiles()






