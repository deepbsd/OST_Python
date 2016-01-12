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
import random
import unittest
import tempfile
import FileTypeLister


suf = ['.py','.txt','.doc','.wp','.lts','.gpg','.jpg',\
        '.gif','.html','.pl','.sh','.mp3','.mp4','.bin'] 

bname = ['one','two.three','four-']

class TestFTL(unittest.TestCase):
    """Tests the FileTypeLister.py program."""

    def setUp(self):
        """Creates a temp dir full of files with various \
            suffixes using the randint() function
        """
        
        #global self.file_count
        self.file_count = random.randint(0, 20)
        #print("File count is {}".format(self.file_count))   # debugging

        #global homedir
        self.homedir = os.getcwd()

        #global dirname
        self.dirname = tempfile.mkdtemp("tempdir")
        os.chdir(self.dirname)
        
        for filenum in range(0, self.file_count):
            for suf_idx in range(0, len(suf)):
                    for bn_idx in range(0, len(bname)):
                        filename = bname[bn_idx]+str(filenum)+suf[suf_idx]
                        #print(filename)    # debugging
                        f = open(filename, 'w')
                        f.write("whatever whatever whatever\n")
                        f.close()

    def test_1(self):
        """Verify that total files listed in tempdir is correct 
        and agrees with suf_dict
        """
        ftl_total = 0
        suf_dict = FileTypeLister.listFiles(self.dirname)
        for value in suf_dict.values():
            ftl_total = ftl_total + int(value)
        total_files = len(bname) * len(suf) * self.file_count
        self.assertEqual(ftl_total, total_files, "Doesn't list correct number of files.")

    def test_2(self):
        "Verify that suf_dict is accurate for files in tempdir"
        suf_dict = FileTypeLister.listFiles(self.dirname)
        for suffix, value in suf_dict.items():
            self.assertEqual(suf_dict[suffix], len(bname)*self.file_count, "Totals wrong for {}".format(suf_dict[suffix]))

    def tearDown(self):
        os.chdir(self.dirname)
        testfiles = glob.glob('*')
        for fn in testfiles:
            os.remove(fn)
        os.chdir(self.homedir)
        os.rmdir(self.dirname)


if __name__ == "__main__":
    unittest.main()








