#!/usr/bin/env python3
#
#           HS_tester.py
#
#     Lesson 5: Persistent Storage
#         for OST Python 2
#
#        by David S Jackson
#         on Jan 31, 2015
#
#       Instructor: Pat Barton
#
"""
This module tests high_score.py.  That module must
accept two parameters: player name and score. (It
also accepts an optional keyword parameter called
'fn', so it is able to operate on a different shelf
file for testing purposes.) The
name will be added to the players if it doesn't exist
already, along with the included score, which will become
the high score for that player.  If a player's existing
score is higher than the one being passed to the function,
the existing score must be returned.  If the newer
score being passed to the function is higher than the
existing score, the newer score must replace the 
existing score.
"""


import high_score
import unittest
import shelve
import os


#testfile = 'testfile1.shlf'

class TestHighScore(unittest.TestCase):
    """
    Test highScore() function of high_score.py
    """

    def setUp(self):
        "create a shelf file for testing"
        #self.fn = testfile
        self.playdb = { 'Brian': 100,
                'Galahad': 150,
                'BlackKnight': 0 }
        
        self.shelf = shelve.open(self.fn, writeback=True)
        for key, value in self.playdb.items():
            self.shelf[key] = value
        self.shelf.close()


    def test_get_new_high(self):
        "New score for 'BlackKnight' SHOULD replace old score"
        observed = high_score.highScore('BlackKnight', 5, fn=self.fn)
        expected = 'BlackKnight: 5'
        self.assertEqual(observed, expected, "It's just a scratch.")


    def test_get_existing_high(self):
        "New score for 'Galahad' should NOT replace old score"
        observed = high_score.highScore('Galahad', 120, fn=self.fn)
        expected = 'Galahad: 150'
        self.assertEqual(observed, expected, "Spank ME!")


    def test_new_player(self):
        "New player 'Guido' should be added to shelf file"
        observed = high_score.highScore('Guido', 200, fn=self.fn)
        expected = 'Guido: 200'
        self.assertEqual(observed, expected, "Way to go, Guido!")


    def tearDown(self):
        "delete test shelf file"
        try:
            os.remove(self.fn)
        except:
            pass



if __name__ == "__main__":
    unittest.main()




