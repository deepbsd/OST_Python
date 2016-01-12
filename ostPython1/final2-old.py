#!/usr/local/bin/python3

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
    print('=' * 60)
    for key, value in word_dict.items():
        if key == 0 :
            continue
        print("{0}\t\t{1}".format(key, value))


def print_hist(word_dict):
    """ This function prints a histogram of word_dict with
    the word lengths displayed as the vertical axis and the
    horizontal axis being the number of times that each word
    length appears in the text.  The length of the horizontal 
    bars is approximately one-quarter scale.

    The length of the horizontal bars is arrived at through
    dividing by four and rounding.  That number, which is a float,
    is then made into an integer, which is used as a multiplier
    for displaying the horizontal bar ('*'). The actual value
    being represented is included within parentheses.

    The bottom scale is very much an approximation, since dividing
    50 by 4 is 12.5, and there is no way to print 1/2 of a 
    character space on this display.  

    Ideally, this function would be replaced by a solution that
    involved the matplotlib module or something similar.  Which
    is too much work for this one assignment, since it involves
    installing a fair amount of extra software for both student 
    and probably instructor??
    """
    print("\nHistorgram for word lengths used in", sys.argv[1])
    print("\nword\nlengths\n=======")
    for length in word_dict.keys():
        if length == 0 :
            continue
        else:
            mult = word_dict[length]/4
            rnd_mult = round(mult, 0)
            rnd_mult = int(rnd_mult)
            print("{0:<2}{1:>}{2}({3})".format(length, '|', '*'*rnd_mult, word_dict[length]))
    print('  '+'|'+'=-'*38+'|')
    print("{0}50|{1}100|{2}150|{3}200|".format(' '*14, ' '*11, ' '*10, ' '*13))
    print("{0:^78}".format("Instances of Word Lengths"))
    print("{0:^78}".format("(Horizontal bars approx. 1/4 scale)"))





### Main program begins
if __name__ == "__main__":

    word_dict = store_count(get_file())
    print_results(word_dict)
    print_hist(word_dict)


