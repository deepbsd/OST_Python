#!/usr/bin/env python3
#
#
#       test_ziparchive.py
#    
#  for OST Python2: Lesson 6 Archives
#
#   by David S Jackson on Feb 1, 2015
#
#     Instructor: Pat Barton
#
#
"""
This module tests the zipit() function in module zip_archive.py
"""

import unittest
import zip_archive
import time
import os
import shutil
import zipfile

class TestZipit(unittest.TestCase):

    def setUp(self):
        """
        Creates a dir with 3 files to archive and a subdir 
        with files to *not* archive
        """
        self.homedir = os.getcwd()
        self.path = "/home/dsj/bin/test_zipit"
        #self.path = "v:\workspace\Archive_Homework\src\test_zipit"
        #self.path = "C:\\Users\\dsj\\My Documents\\Aptana Studio 3 Workspace\\Archives\src\\test_zipit"
        self.path = os.path.normpath(self.path)
        self.zip_filename = os.path.join(self.homedir, "zip_test.zip")
        os.mkdir(self.path)
        self.filenames = ['first', 'second', 'third']
        for fn in self.filenames:
            f = open(os.path.join(self.path, fn), 'w')
            f.close()
        self.fakedir = os.path.join(self.path, 'dont_archive')
        os.mkdir(self.fakedir)
        for fn in self.filenames:
            f = open(os.path.join(self.fakedir, fn), 'w')
            f.close()


    def test1(self):
        zip_archive.zipit(fn=self.zip_filename, dirpath=self.path)
        testzipfile = zipfile.ZipFile(self.zip_filename, 'r')
        expected = ['test_zipit/first', 'test_zipit/second', 'test_zipit/third']
        lst = testzipfile.namelist()
        testzipfile.close()
        observed = sorted(lst)
        self.assertEqual(observed, expected)

    def tearDown(self):
        os.remove(self.zip_filename)
        try:
            shutil.rmtree(self.path, ignore_errors=True)
        except IOError:
            pass


if __name__ == "__main__":
    unittest.main()

