#!/usr/local/bin/python3
#
#       Project File Handling
#
#       OST Python2 Lesson 4
#
#       by David S. Jackson
#       on January 12, 2015
#
#    for Pat Barton, Instructor
#
import unittest
import os
import fileops

class TestReadWriteFile(unittest.TestCase):
    """Test case to verify list read/write functionality"""

    def setUp(self):
        """This function is run before each test"""
        #self.fixture_file= r"v:\workspace\FileHandling\src\test-read-write.txt"
        self.fixture_file= r"test-read-write.txt"
        self.fixture_list = ["my", "written", "text"]
        self.fixture_list_empty_strings = ["my", "", "", "written", "text"]
        self.fixture_list_trailing_empty_strings = ["my", "written", "text", "", ""]

    def verify_file(self, fixture_list):
        """Verifies that a given list, when written to a file, is
        returned by reading the same file"""
        fileops.write_list(self.fixture_file, fixture_list)
        observed = fileops.read_list(self.fixture_file)
        self.assertEqual(observed, fixture_list, "%s does not equal %s" % (observed, fixture_list))


    def test_read_write_list(self):
        self.verify_file(self.fixture_list)

    def test_read_write_list_empty_strings(self):
        self.verify_file(self.fixture_list_empty_strings)

    def test_read_write_list_trailing_empty_strings(self):
        self.verify_file(self.fixture_list_trailing_empty_strings)

    def tearDown(self):
        """This function is run after each test."""
        try:
            os.remove(self.fixture_file)
        except OSError:
            pass

if __name__ == "__main__":
    unittest.main()


