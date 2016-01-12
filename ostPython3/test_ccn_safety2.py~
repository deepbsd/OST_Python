#!/usr/bin/env python3
#
#
#       test_ccn_safety.py
#
#    Lesson 6: Compiling and Flagging REgexes
#
#     by David S. Jackson
#          4/30/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
Lesson 6 uses a compiled regex.  The tests stay the same, mostly
"""
import unittest
import re
from ccn_safety2 import text, num_safe

newtext = """\
Don't leave credit cards lying around with numbers like
1234 5678 9012 3456 or like 0987-6543-2109-8765 or even
1357-9135-7913-5791.  That is really dumb, because bad
guys can steal you dry and make your life a living hell.
So don't do it!"""

fixed_txt = """\
Have you ever noticed, in television and movies, that phone numbers 
and credit cards are obviously fake numbers like 555-123-4567 or
CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as
CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts."""

txt2test = """\
Have you ever noticed, in television and movies, that phone numbers 
and credit cards are obviously fake numbers like 555-123-4567 or
5555-5555-5555-5555? It is because a number that appears to be real, such as
1234-5678-1234-5678, triggers the attention of privacy and security experts."""


class Test_CCN_Safe(unittest.TestCase):
    """
    Tests the num_safe() method from ccn_safety.py
    """
    def test_sub(self):
        "Tests that simple substitutions are okay"
        expected = "CCN REMOVED FOR YOUR SAFETY"
        self.assertEqual(num_safe("1234-1234-1234-1234"), expected)
        self.assertEqual(num_safe("1234 1234 1234 1234"), expected)

    def test_txt(self):
        "Entire passages with ccn's should be correct."
        self.assertEqual(num_safe(txt2test), fixed_txt)

    def test_re_mojo(self):
        """
        Test that 'findall(pattern, num_safe(newtext))' gets returned with
        properly fixed CCNs"
        """
        #pattern = r"(X{4}-X{4}-X{4}-\d{4})"
        pattern = "CCN REMOVED FOR YOUR SAFETY"
        expected = "CCN REMOVED FOR YOUR SAFETY"
        test = re.findall(pattern, num_safe(newtext))
        self.assertEqual(test[0], expected)
        self.assertEqual(test[1], expected)
        self.assertEqual(test[2], expected)
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
        fixed_pattern =  "CCN REMOVED FOR YOUR SAFETY"
        expected = "CCN REMOVED FOR YOUR SAFETY"
        m = re.finditer(fixed_pattern, num_safe(newtext))
        expectedlist = [ expected, expected, expected]
        self.assertEqual([ a.group() for a in m ], expectedlist)




if __name__ == "__main__":
    unittest.main()



