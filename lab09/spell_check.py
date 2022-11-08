#!/usr/bin/env python3

'''
Title:      spell_check.py
Abstract:   Simple spell checker using different data structures.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   25 minutes
Date:       11/08/2022
Questions:

    1. What is the average time complexity of searching the words list?

        ????

    2. What is the average time complexity of searching the words set?

        ????

    3. How would you modify the spellchecker to ignore punctuation (ie.
    "donate," or "anyone.")?

        ????

    4. How fast is using a set vs a list to perform spell check?

        ????
'''

import sys

# Constants

WORDS_PATH ='/usr/share/dict/words'

# Functions

def load_words_list(words_path=WORDS_PATH):
    ''' Load words file into list. 

    >>> words = load_words_list()
    >>> isinstance(words, list)
    True

    >>> 'notre' in words
    True
    
    >>> 'dame' in words
    True
    
    >>> 'football' in words
    True

    >>> 'asdfafdasdfjkl;j' in words
    False
    '''
    pass

def load_words_set(words_path=WORDS_PATH):
    ''' Load words file into set. 

    >>> words = load_words_set()
    >>> isinstance(words, set)
    True

    >>> 'notre' in words
    True
    
    >>> 'dame' in words
    True
    
    >>> 'football' in words
    True

    >>> 'asdfafdasdfjkl;j' in words
    False
    '''
    pass

# Main Execution

def main(stream=sys.stdin, use_set=False):
    ''' For each word in standard input, check if it is in the words file.

    If use_set is True, load the words into a set, otherwise, load the words
    into a list.
    
    You should ignore case when checking, but print the original word if it is
    not in the words file.

    >>> import copy, io
    >>> sio = io.StringIO('Notre Dame Football\\nFreeman era\\nJust runthedamnball\\n') 
    >>> main(copy.copy(sio))
    runthedamnball
    
    >>> main(copy.copy(sio), True)
    runthedamnball
    '''
    pass

if __name__ == '__main__':
    main(use_set=len(sys.argv) > 1 and sys.argv[1] == '-s')
