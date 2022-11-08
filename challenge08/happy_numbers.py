#!/usr/bin/env python3

'''
Title:      happy_numbers.py
Abstract:   Determine if a number is a happy number or not using memoization.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   30 minutes
Date:       11/14/2022
Questions:

    1. How is seen used in is_happy()?

        ????

    2. How is table used in is_happy() to implement memoization?

        ????

    3. How many happy numbers are there between 1 and 100 (inclusive)?

        ????
'''

from table import Map

import sys

# Functions

def is_happy(n, seen, table):
    ''' Return whether or not n is a happy number.

    >>> is_happy(19, Map(), Map())
    True

    >>> is_happy(2, Map(), Map())
    False

    >>> is_happy(68, Map(), Map())
    True

    >>> is_happy(75, Map(), Map())
    False

    >>> is_happy(91, Map(), Map())
    True
    '''
    pass

# Main Execution

def main(stream=sys.stdin):
    ''' For each number in standard input, determine if it is a happy number,
    and print it out.

    >>> import io
    >>> main(io.StringIO('19\\n2\\n68\\n75\\n91\\n'))
    Is 19 Happy?: Yes
    Is 2 Happy?: No
    Is 68 Happy?: Yes
    Is 75 Happy?: No
    Is 91 Happy?: Yes
    '''
    pass

if __name__ == '__main__':
    main()
