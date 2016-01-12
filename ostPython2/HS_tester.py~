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
import tempfile
import shelve
import os
import shutil


testfile = 'testfile1.shlf'

class TestHighScore(unittest.TestCase):
    """
    Test highScore() function of high_score.py
    """

    def setUp(self):
        "create a shelf file for testing"
        self.homedir = os.getcwd()
        self.testdir = tempfile.mkdtemp("tempdir")
        self.name_score_exp = [ ('Todd', 305, 'Todd: 305'),  #higher_score
                                ('Bill', 150, 'Bill: 300'),  #lower_score
                                ('BlackKnight', 10, 'BlackKnight: 10') #new_player
                              ]
        os.chdir(self.testdir)


    def test_get_new_high(self):
        "New score for 'Todd' SHOULD replace old score"
        name, score, expected = self.name_score_exp[0]
        observed = high_score.highScore(name, score)
        self.assertEqual(observed, expected, "I'm not quite dead yet.")


    def test_get_existing_high(self):
        "New score for 'Bill' should NOT replace old score"
        name, score, expected = self.name_score_exp[1]
        observed = high_score.highScore(name, score)
        self.assertEqual(observed, expected, "Spank ME!")


    def test_new_player(self):
        "New player 'BlackKnight' should be added to shelf file"
        name, score, expected = self.name_score_exp[2]
        observed = high_score.highScore(name, score)
        self.assertEqual(observed, expected, "It's just a scratch!")


    def tearDown(self):
        # Make tearDown() get rid of everything!!!
        "delete test shelf file"
        os.chdir(self.homedir)
        shutil.rmtree(self.testdir, ignore_errors=True)



if __name__ == "__main__":
    unittest.main()




