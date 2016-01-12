#!/usr/local/bin/python3
#
#  Another dandy copied program for
#  OST Python2  Lesson 3
#   by David S. Jackson
#   Instructor:  Pat Barton
#
#
"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - 
This is a demo.
"""
"""
Here are your instructions:


    Make a TestDrivenDevelopment_Homework project and assign it to the
    Python2_Homework working set.

    Copy the setupDemo.py file from the TestDrivenDevelopment/src folder to the
    TestDrivenDevelopment_Homework/src folder.

    Modify it so that:

        oThe test_1() method includes code to verify that the test directory
        contains only the files created by the for loop. Hint: You might create
        a set containing the list of three filenames, and then create a set
        from the os.listdir() method.

        oA test_3() method creates a binary file that contains exactly a
        million bytes, closes it and then uses os.stat to verify that the file
        on disk is of the correct length (with os.stat, statinfo.st_size
        returns the size in bytes).
         

        How long did it take you to complete this project? What's this?
         (This estimate helps us verify time projections for courses,
         anonymously. It is not part of your evaluation.) 

"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)

    def test_1(self):
        "Verify creation of files is possible"
        for filename in ("this.txt", "that.txt", "the_other.txt"):
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)

    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()

