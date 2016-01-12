#!/usr/bin/env python3




import unittest
import library
import os
import glob

class TestLibrary(unittest.TestCase):
    def setUp(self):
        #self.lib_fn = r'v:\workspace\PersistentStorage\src\lib.shelve'
        self.lib_fn = r'lib.shelve'
        self.lib = library.Library(self.lib_fn)
        self.fixture_author1 = library.Author('Octavia', 'Estelle', 'Butler')
        self.fixture_book1 = library.Book('0907083100', 'Kindred', [self.fixture_author1])
        self.fixture_author2 = library.Author('Robert', 'Anson', 'Heinlein')
        self.fixture_book2 = library.Book('0441790348', 'Stranger in a Strange Land', [self.fixture_author2])
        self.lib.add(self.fixture_book1)
        self.lib.add(self.fixture_book2)

    def testGetByIsbn(self):
        observed = self.lib.get_by_isbn(self.fixture_book1.isbn)
        self.assertEqual(observed, self.fixture_book1)

    def testGetByTitle(self):
        observed = self.lib.get_by_title(self.fixture_book2.title)
        self.assertEqual(observed, self.fixture_book2)

    def testGetByAuthor(self):
        observed = self.lib.get_by_author(self.fixture_book1.authors[0])
        self.assertEqual(observed, self.fixture_book1)

    def tearDown(self):
        self.lib.close()
        shelve_files = glob.glob(self.lib_fn + '*')
        for fn in shelve_files:
            os.remove(fn)


if __name__ == "__main__":
    unittest.main()
