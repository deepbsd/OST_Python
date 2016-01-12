#!/usr/local/bin/python3
#
#   final2.py
#
#   David S. Jackson
#   December 31, 2014
#   OST Python1, Lesson 16, Attempt 2
#
#   Happy New Year!
#
""" 
This program is the third and final exercise of the 
OST Python1 course.  It's an extension of final.py and uses 
the same file(s) as input(s) to process.  This file to process
must be provided as an argument when invoking this program.

The program not only provides the same tabular output that
final.py does, but it also provides a histogram of that data
in a graphical presentation.  
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
    print("Word            Number of times word this")
    print("Length          Length appears in", sys.argv[1])
    print('=' * 45)
    for key, value in sorted(word_dict.items()):
        if key == 0 :
            continue
        print("{0:>4d}\t\t{1:>4d}".format(key, value))


def print_hist(word_dict):
    """ This function prints a histogram of the data in word_dict.
    The histogram is a vertical scale of the frequency of word lengths
    in sys.argv[1].  Each asterisk is worth about 20 instances, so no
    asterisks appear for lengths less than 2, nor lengths greater than
    11, at least in declaration.txt.  
    """
    print('\nUses in\n{0:<}'.format(sys.argv[1]))
    print('===============')
    y_max = max(word_dict.values())
    max_y = (round(y_max/100)*100) + 100
    x_max = max(word_dict.keys())
    for row in range(max_y, 0, -20):
        if row % 100 == 0:
            print("{0:>3d}".format(row) + " -| ", end="")
        else:
            print('     | ', end="")
        for num in range(1, x_max+1, 1):
            if num in word_dict.keys() and word_dict[num] >= row:
                print('***', end="")
            else:
                print('   ', end="")
        print()
    # Print the index and scale at bottom
    print("{0:>3d}".format(0) + " -+-", end="")
    for n in range(1, max(word_dict.keys())+1):
        print("-+-", end="")
    print()
    print('     |  1', end="")
    for n in range(2, max(word_dict.keys())+1 ):
        print("{0:>3d}".format(n), end="")
    print('\n\t{0} {1}'.format('Lengths of Words used in', sys.argv[1]))
    print('\t({0})'.format('Each * represents about 20 uses'))




### Main program begins
if __name__ == "__main__":

    word_dict = store_count(get_file())
    print_results(word_dict)
    print_hist(word_dict)


