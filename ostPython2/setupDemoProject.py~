#!/usr/local/bin/python3
#
#   Unittest Project
#
#  OST Python2  Lesson 3
#
#   by David S. Jackson
#      Jan 11, 2015
#   Instructor:  Pat Barton
#
#
"""
Demonstration of setUp and tearDown.
Temporary test directory is created, three files are
created in that directory.  If those files and only 
those three files are present in the directory, the
test passes.  test_3 creates a binary file of exactly 
one million bytes.  All temp files and directories 
are removed by tearDown()

Test 3 imports the struct file in order to create a binary 
file using the 'pack' method.  
"""
import unittest
import tempfile
import shutil
import glob
import struct
import os

class FileTest(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)

    def test_1(self):
        "Verify creation of files is possible and files are exact"
        names = ["this.tst","that.txt","the_other.txt"]
        for filename in names:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
        files = os.listdir()
        self.assertTrue(set(names)==set(files), "Files not equal to glob.")
        
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")

    def test_3(self):
        "Create a binary file that contains exactly a million bytes"
        packed = struct.pack('>i4sh', 7, b'spam', 8) # sb 10 bytes long
        outfile = open("binout.bin", 'wb')
        for num in range(0,100000):
            outfile.write(packed)
        outfile.close()
        info = os.stat(r"binout.bin")
        size = info.st_size
        self.assertTrue(size==1000000, "Binary file wrong size")

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()

