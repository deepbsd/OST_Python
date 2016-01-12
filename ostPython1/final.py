#!/usr/bin/env python3
#
#            
#
#   Word Length Counting Tool
#          final.py
#
#   David S. Jackson
#   December 31, 2014
#   OST Python1, Lesson 16, Attempt 2
#
#
"""
This program is a final exercise for Python1 at OST.  Program accepts 
a filename as an argument.  This filename should be a text file to
process, and it should be in the current working directory, or the 
argument should be the path to this this filename.  The keys to the 
dictionary are the list of word lengths in the text.  If no filename is
provided as an argument, an error is returned to the user and the program 
exits.  Program requires sys module.  The printing funtion removes any
zero length words from the output.

Additionally, there is a function called test_out() that can be called
to look at the values in the word_dict dictionary. 

You can now just add '-t' after the name of the file you wish to analyze.  
You can see exactly what words are being measured for length.  Probably 
best to pipe the std_out to your favorite pager.
Example:

    final.py declaration.txt -t | less

The -t switch is new and will allow you to bypass the other functions in
the program when you just want to look at your data for a sanity check.

"""

import sys

def word_len(raw_word):
    """ Function returns length of word after removing punctuation 
    and special characters. This used by store_count() 
    """
    raw_word = raw_word.strip()
    punct = "!@#$%^&*()_+=-{}?<>[]\\;:',./"
    raw_word = raw_word.strip(punct)
    word = raw_word
    for c in raw_word :
        if c in punct:
            word = raw_word.replace(c, "")
    return len(word)



def store_count(wordlist):
    """ keeps a dictionary of word lengths with usage counts 
    for each word length. Each word length is a key whose value is 
    the number of times that word length is used.  This function 
    calls word_len()
    """
    word_count = {}
    for word in wordlist:
        if word_len(word) in word_count.keys():
            word_count[word_len(word)] = word_count[word_len(word)] + 1
        else:
            word_count[word_len(word)] = 1
    return word_count


def get_file():
    """ Func tests for for sys.argv[1].  Catches exception and 
    prompts user for filename argument. Returns wordlist from
    text file (sys.argv[1]).  Also, it's best to remove newlines
    and extra spaces now.
    """
    try:
        infile = open(sys.argv[1], 'r')
        filehandle = infile.read()
        filehandle = filehandle.replace("\n", " ")
        filehandle = filehandle.replace("  ", " ")
        wordlist = filehandle.split(" ")
        infile.close()
        return wordlist
    except (FileNotFoundError, IndexError):
        print("WARNING: Must provide path to filename as argument to", sys.argv[0])
        exit()
    except Exception as message:
        print("Problem: {0}".format(message))
        exit()


def print_results(word_dict):
    """ Function prints results of processing sys.argv[1] 
    This function does NOT print keys whose value is zero (0)
    """
    print('\n\n')
    print("word             number of times word this")
    print("length           length appears in", sys.argv[1])
    print('=' * 45)   # changed to 45
    for key, value in sorted(word_dict.items()):  # added sorted()
        if key == 0 :
            continue
        print("{0:>4d}\t\t{1:>4d}".format(key, value))  # added .format()


def test_out():
    """ This is a function to test the accuracy of the program.  
    It writes a list of the words to standard output and sorts them 
    by their length.  You can glance through the sorted output and see 
    if there are any glaring problems. Probably best to use your
    favorite pager when using this function.
    """
    big_wordlist = []
    punct = "!@#$%^&*()_+=-{}?<>[]\\;:',./"
    infile = get_file()
    for raw_word in infile:
        raw_word = raw_word.strip(punct)
        word = raw_word
        for c in raw_word :
            if c in punct:
                word = raw_word.replace(c, "")
        line = str(len(word)) + " " + word
        big_wordlist.append(line)
    big_wordlist = sorted(big_wordlist)
    for item in big_wordlist:
        print(item)



### Main program begins
if __name__ == "__main__":

    try:
        if sys.argv[2] == '-t':
            test_out()
    except IndexError:
        print("Not analyzing raw data...")
        word_dict = store_count(get_file())
        print_results(word_dict)

