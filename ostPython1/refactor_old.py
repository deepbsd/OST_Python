#!/usr/local/bin/python3

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')

def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which 
    case the word is correctly capitalized

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    lst_of_words = title.lower().split()
    num_of_words = len(lst_of_words)
    if num_of_words < 1:
        return ''
    new_title = lst_of_words.pop(0)
    new_title = new_title[0].upper() + new_title[1:]
    tpl_of_words = tuple(lst_of_words)
    for word in tpl_of_words:
        prep_word = False
        for prep in small_words:
            if prep == word:
                new_title = new_title + ' '
                new_title = new_title + word
                prep_word = True
                break
        if prep_word == True:
            continue
        new_title = new_title + ' '
        new_title = new_title + word[0].upper()
        new_title = new_title + word[1:]
    return new_title


def _test():
    import doctest, refactor
    return doctest.testmod(refactor)

if __name__ == "__main__":
    _test()






