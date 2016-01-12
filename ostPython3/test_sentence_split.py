#!/usr/bin/env python3

import unittest

from sentence_split import sentence_split

text = "Hello!  My name is Dave.  What is yours?  I hope you enjoyed this class!"

class TestRegex(unittest.TestCase):

    def test_split_sentence(self):
        numbers = sentence_split(text)
        self.assertEqual(len(numbers), 4)


if __name__ == "__main__":
    unittest.main()
