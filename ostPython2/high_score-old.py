#!/usr/bin/env python3
#
#
#            high_score.py
#
#       Project for OST Lesson 5: 
#          Persistent Storage
#
#         by David S. Jackson
#
#       Instructor: Pat Barton
#
#
"""
This module can create, list, and update a database of high scores
for players, using the shelve module.

"""
import shelve


fn = "player_scores.shlf"
testfile = "testfile.shlf"

def highScore(name, score):
    """
    This function will return the high score for a player in a database.
    The function requires a player's name and a score.  If the given score
    is higher than the player's existing high score, the database will be 
    updated with the new high score.  If the given score is lower, the 
    existing high score will be returned.  If a new player name is given
    then a new player name will be added to the data base with the given
    score as that player's current high score.
    """
    score = int(score)
   
    shelf = shelve.open(fn, writeback=True)
    
    if name in shelf.keys() and score > shelf[name]:
        shelf[name] = score
    if name not in shelf.keys():
        shelf[name] = score
    player_dat = name + ': ' + str(shelf[name])
    shelf.close()
    return player_dat


def makeScores():
    """
    This function creates an initial database of players and scores
    in a shelf file. 
    """

    db = {'Jim': 225,
            'Bill': 300,
            'Todd': 302,
            'Ned': 298,
            'Babe': 320 }

    shelf = shelve.open(fn, writeback=True)
    for key, value in db.items():
        shelf[key] = value
    shelf.close()


def listScores():
    """
    listScores() simply prints to the screen those entries contained
    in the player high scores shelf.  
    """
    shelf = shelve.open(fn)
    for key, value in shelf.items():
        print("Key: {}\tValue: {}".format(key, value))
    shelf.close()


if __name__ == "__main__":
    makeScores()
    #print(highScore('Jim', 305))
    data = highScore('Dave', 270)
    print(data, '\n')
    listScores()

