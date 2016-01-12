#!/usr/bin/env python3

"""
Test of groffle.py:  We're trying to establish that groffle_faster(mass, density)
is at least 33.3% of the time required for groffle_slow(mass, density)
"""

import unittest
from groffle import groffle_slow, groffle_faster

from timeit import Timer

class TestGroffle(unittest.TestCase):

    def setUp(self):
        #print(groffle_faster(mass, density))
        self.groffle_slow = groffle_slow(mass, density)
        self.groffle_faster = groffle_faster(mass, density)
        slowtime = Timer("total = groffle_slow(mass, density)", "from __main__ import groffle_slow, mass, density")
        fastertime = Timer("total = groffle_faster(mass, density)", "from __main__ import groffle_faster, mass, density")
        self.slowtime = slowtime.timeit(number=1000)
        self.fasttime = fastertime.timeit(number=1000)

    def test_speeds(self):
        self.expected_time = 0.34 * self.slowtime
        self.assertLessEqual(self.fasttime, self.expected_time)

    def test_accuracy(self):
        self.assertAlmostEqual(self.groffle_slow, self.groffle_faster, places=10)



if __name__ == "__main__":
    mass = 2.5
    density = 12.0
    unittest.main()


