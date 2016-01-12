#!/usr/bin/env python3
#
#
#       test_math_quiz.py
#
#    Lesson 13: Time Computations
#
#     by David S. Jackson
#          6/4/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
test_math_quiz.py is a simple test of the time_it() function in math_quiz.py.
The test comprises a start and an end time being submitted to time_it() where
end is known to be 30 seconds after start.  If time_it() measures exactly 30
seconds, then it passes the test.  A timedelta is used to create the end time
value, so any time can be used for the duration between start and end.

Further, time_it() is tested to see whether it accepts bad input.  If it
doesn't raise the 'BadTimeObjError' exception, the function fails the test.
"""

import unittest
from datetime import datetime, timedelta
from math_quiz import *


class MathQuiz(unittest.TestCase):


    def test_time_it(self):
        "Test the time_it function"
        # the time between self.start and self.end should be 30 sec
        self.start = datetime.now()
        self.duration = timedelta(seconds=30)
        self.end = self.start+self.duration

        # if time_it() works, start and end will equal duration.seconds...
        self.assertEqual(time_it(self.start, self.end), self.duration.seconds)
        # test that time_it() raises exception for bad input...
        self.assertRaises(BadTimeObjError, time_it, 'first', 'second')

    def test_randint(self):
        "Tests the random number generator part of math_quiz.py"
        numlist = []
        for num in range(0,1000):
            numlist.append(gennum())

        # out of 1000 numbers, the min and max better be 1 and 10
        self.assertGreaterEqual(min(numlist), 1)
        self.assertLessEqual(max(numlist), 10)



if __name__ == "__main__":
    unittest.main()
