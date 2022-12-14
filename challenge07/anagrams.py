#!/usr/bin/env python3

'''
Title:      anagrams.py
Abstract:   Determine if two words are anagrams.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   30 minutes
Date:       11/07/2022
Questions:

    1. What is the worst-case time complexity for count_letters()?

        O(nlogn)

    2. What is the worst-case time complexity ofr is_anagram()?

        O(nlogn)
'''

from treap import Map

import sys

# Functions

def count_letters(word):
    ''' Counts the occurrences of each letter in word and stores it in a Map
    (case insensitive).

    >>> counts = count_letters('aBbCcC')
    >>> counts.lookup('a')
    1
    >>> counts.lookup('b')
    2
    >>> counts.lookup('c')
    3
    >>> counts.lookup('d')
    '''
    pass

def is_anagram(word_a, word_b):
    ''' Returns whether or not two words are anagrams.

    >>> is_anagram('anna', 'naan')
    True

    >>> is_anagram('banana', 'aNaNaB')
    True

    >>> is_anagram('SiLeNt', 'listen')
    True

    >>> is_anagram('KeK', 'eek')
    False

    >>> is_anagram('Nope', 'Topen')
    False

    >>> is_anagram('taco', 'cat')
    False
    '''
    pass

# Main Execution

def main(stream=sys.stdin):
    ''' For each pair of words on each line, determine if they are anagrams,
    and print out the result.

    >>> import io
    >>> main(io.StringIO('taco cat\\nanna naan\\nSiLeNt listen\\n'))
    taco and cat are not anagrams!
    anna and naan are anagrams!
    SiLeNt and listen are anagrams!
    '''
    pass

if __name__ == '__main__':
    main()
