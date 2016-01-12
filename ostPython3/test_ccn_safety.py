#!/usr/bin/env python3
#
#
#       test_ccn_safety.py
#
#    Lesson 5: More on Regex
#
#     by David S. Jackson
#          4/28/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
This module tests the num_safe method in ccn_safety.py.  I tried to 
go above and beyond the requirements of the assignment and actually
check for "-" and " " between the credit card numbers.  The function
returns merely the corrected pattern, nothing else.

This test includes a 'newtext' variable with more credit card numbers, 
both of the type with "-"'s and with spaces.  Further, this test
module tests the assignment text against a corrected version of the
assignment text.

Lastly, a 're_mojo' test gives me a little bit of playtime with 
re.findall() and also some practice at re.searching the corrected
version of test texts.  
"""
import unittest
import re
from ccn_safety import text, num_safe

newtext = """\
Don't leave credit cards lying around with numbers like
1234 5678 9012 3456 or like 0987-6543-2109-8765 or even
1357-9135-7913-5791.  That is really dumb, because bad
guys can steal you dry and make your life a living hell.
So don't do it!"""

fixed_txt = """\
Have you ever noticed, in television and movies, that phone numbers and
credit cards are obviously fake numbers like 555-123-4567 or
XXXX-XXXX-XXXX-5555? It is because a number that appears to be real, such as
XXXX-XXXX-XXXX-5678, triggers the attention of privacy and security experts."""

txt2test = """\
Have you ever noticed, in television and movies, that phone numbers and
credit cards are obviously fake numbers like 555-123-4567 or
5555-5555-5555-5555? It is because a number that appears to be real, such as
1234-5678-1234-5678, triggers the attention of privacy and security experts."""


class Test_CCN_Safe(unittest.TestCase):
    """
    Tests the num_safe() method from ccn_safety.py
    """
    def test_sub(self):
        "Tests that simple substitutions are okay"
        self.assertEqual(num_safe("1234-1234-1234-1234"), "XXXX-XXXX-XXXX-1234")
        self.assertEqual(num_safe("1234 1234 1234 1234"), "XXXX-XXXX-XXXX-1234")

    def test_txt(self):
        "Entire passages with ccn's should be correct."
        self.assertEqual(num_safe(txt2test), fixed_txt)

    def test_re_mojo(self):
        """
        Test that 'findall(pattern, num_safe(newtext))' gets returned with
        properly fixed CCNs"
        """
        pattern = r"(X{4}-X{4}-X{4}-\d{4})"
        test = re.findall(pattern, num_safe(newtext))
        self.assertEqual(test[0], 'XXXX-XXXX-XXXX-3456')
        self.assertEqual(test[1], 'XXXX-XXXX-XXXX-8765')
        self.assertEqual(test[2], 'XXXX-XXXX-XXXX-5791')
        self.assertEqual(len(test), 3)

    def test_no_ccns(self):
        """
        Shouldn't be any raw CCNs in num_safe(text). 'text' 
        is imported from ccn_safety.py.
        """
        pattern = r"(\d{4}(-| )\d{4}(-| )\d{4}(-| )\d{4})"
        self.assertIsNone(re.search(pattern, num_safe(text)))

    def test_iter(self):
        """
        Need some practice with re.finditer()
        """
        pattern = r"((X{4}-){3}\d{4})"
        m = re.finditer(pattern, num_safe(newtext))
        expected = [ 'XXXX-XXXX-XXXX-3456', 
                'XXXX-XXXX-XXXX-8765', 
                'XXXX-XXXX-XXXX-5791']
        self.assertEqual([ a.group() for a in m ], expected)




if __name__ == "__main__":
    unittest.main()



