#!/usr/local/bin/python3
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
    small_words = ['of','to','for','by','in','on','if']
    new_str = ""
    for word in s.split():
        if word.lower() not in small_words:
            new_str = new_str + " " + word[0].upper()+word[1:].lower()
        else:
            new_str = new_str + " " + word.lower()
    return new_str.lstrip()
    


class TestTitle(unittest.TestCase):
    
    def test_correct_title(self):
        self.assertEqual(title('A Tale of Two Cities'), 'A Tale of Two Cities', "Only 'of' should be lower case")
    def test_incorrect_title(self):
        self.assertEqual(title('tale of two cities'), 'Tale of Two Cities', "Only 'of' should be lower cased")
    def test_McName(self):
        self.assertEqual(title('McBride goes home'), 'Mcbride Goes Home', 'title method goofs here')
    def test_weirdtitle(self):
        self.assertEqual(title('123s and ABCs'), '123s And Abcs', 'Goofiness of original method not fully duplicated.')
    

if __name__ == "__main__":
    unittest.main()

        
