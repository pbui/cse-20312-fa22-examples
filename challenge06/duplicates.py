#!/usr/bin/env python3

'''
Title:      duplicates.py
Abstract:   Determine whether or not a line of words contains any duplicates.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   30 minutes
Date:       10/31/2022
Questions:

    1. What is the average time complexity of detect_duplicates()?

        ????

    2. What is the worst-case time complexity of detect_duplicates()?

        ????

    3. What is the worst-case space complexity of detect_duplicates()?

        ????

    4. How would you modify the program to make it case in-sensitive?

        ????
'''

import sys

from set import Set

# Functions

def detect_duplicates(words):
    ''' Return whether or not the sequence of words contains a duplicate.

    >>> detect_duplicates('a b c'.split())
    False

    >>> detect_duplicates('a b a'.split())
    True

    >>> detect_duplicates('a b c b e f'.split())
    True
    '''
    pass

# Main Execution

def main(stream=sys.stdin):
    ''' For each line of words, determine if there are any duplicates.

    >>> import io
    >>> main(io.StringIO('a b c\\na b a\\na b c b e f\\n'))
    False
    True
    True
    '''
    pass

if __name__ == '__main__':
    main()
