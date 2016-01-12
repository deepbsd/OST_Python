#!/usr/bin/env python3
#
#    UnitTest Exercise for title(s): Function
#                    titleS.py
#       Another quality exercise by David Jackson
#         For OST Python 2 and Instructor Pat Barton
#             Lesson 2  Project 1
#                 January 8, 2015
#
"""
This module defines a function and tests it using a TestTitleS class
that I define in here.  TitleS in the exercise description does
not perform like the standard Python string.title() method.  Instead,
it uppercases the first character and leaves the rest of the
characters alone.  

The assignment function was:  return s[0].upper.()+s[1:]
However, the standard title() method would be more like:
return s[0].upper.()+s[1:].lower() for each word in the string
And this is my correction to the exercise so it behaves more
like the standard Python string.title() method.

I was not able to duplicate a string like '123s and ABCs'.
str.title() would return '123S and Abcs'.  I could not find a way
to keep the return '123S'
"""
import unittest

def title(s):
    '''Corrected function returns string capitalized like standard
    Python string.title() method.  '''
    small_words = ['of','to','for','by','in','and','on','if']
    new_str = ""
    for word in s.split():
        if word.lower() not in small_words:
            new_str = new_str + " " + word[0].upper()+word[1:].lower()
        else:
            new_str = new_str + " " + word.lower()
    return new_str.lstrip()
    


class TestTitle(unittest.TestCase):
    
    def test_correct_title(self):
        cor_title = 'A Tale of Two Cities'
        cor_title_expected = 'A Tale of Two Cities'
        self.assertEqual(title(cor_title), cor_title_expected, "Test matched built-in: Input: {}; Expected: {}; Produced: {}".format(cor_title, cor_title.title(), title(cor_title)))

    def test_incorrect_title(self):
        incor_title = 'a tale of two cities'
        cor_title_expected = 'A Tale of Two Cities'
        self.assertEqual(title(incor_title), cor_title_expected, "Input: {}; Expected: {} matches Built-in: {}".format(incor_title, cor_title_expected, incor_title.title()))

    def test_weirdtitle(self):
        weird_title = '123s and ABCs'
        weird_title_expected = '123s and Abcs'
        weird_title_correct = '123s and ABCs'
        self.assertEqual(title(weird_title), weird_title_expected, "Requires Hand Editing--Expected: {}; built-in: {}; proper: {}".format(weird_title_expected, weird_title.title(), weird_title_correct))

    def test_McName(self):
        mc_title = 'McBride goes home'
        mc_title_expected = 'Mcbride Goes Home'
        mc_title_correct = 'McBride Goes Home'
        self.assertEqual(title(mc_title), mc_title_expected, "Built-in is {}; Should be {}; Must hand edit".format(mc_title.title(), mc_title_correct))
    
    def test_Irish_Priest(self):
        test_name = "o'leary"
        expected = "O'Leary"
        self.assertNotEqual(title(test_name), test_name.title(), "Title case was not executed according to title() method.  Expected: {}; built-in: {}; upgraded: {}".format(expected, test_name.title(), title(test_name)))


if __name__ == "__main__":
    unittest.main()

        
