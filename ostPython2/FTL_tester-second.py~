#!/usr/local/bin/python3
#
#  File Type Lister Tester (FTL_tester.py)
#       (tests FileTypeLister.py module)
#
#           by David S. Jackson
#       for OST Python 2 on Jan 15, 2015
#
#            Instructor Pat Barton
#
"""This program calls the unittest module and tests the accuracy
of the program called FileTypeLister.py.  This module lists all
files in the designated directory (dirpath) by suffix and counts
the number of occurances for each file type according to suffix.
This unittest tests the accuracy of that program with some tests.
"""

import os
import glob
import unittest
import tempfile
import FileTypeLister



class TestFTL(unittest.TestCase):
    """Tests the FileTypeLister.py program."""

    def setUp(self):
        """
        Creates tempdir for testing and changes to that test directory
        """
        self.homedir = os.getcwd()
        self.testdir = tempfile.mkdtemp()
        os.chdir(self.testdir)
        

    def test_1(self):
        """
        Verify that total files listed in tempdir is correct 
        and agrees with suf_dict
        """
        os.mkdir('bogus.dir') # should not report this...
        for fn in ["test1.doc", "test2.doc", "long.file.name.ext.tz", "no_ext", "PatsFile.zip"]:
            f = open(fn, 'w').close()
        expected = {".doc":2, ".tz":1, "":1, ".zip":1}
        observed = FileTypeLister.listFiles(os.getcwd())
        self.assertEqual(observed, expected, "Huston, We Have a Problem!")


    def tearDown(self):
        os.chdir(self.testdir)
        os.rmdir('bogus.dir')
        testfiles = glob.glob('*')
        for fn in testfiles:
            os.remove(fn)
        os.chdir(self.homedir)
        os.rmdir(self.testdir)


if __name__ == "__main__":
    unittest.main()








