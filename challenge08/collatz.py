#!/usr/bin/env python3

'''
Title:      collatz.py
Abstract:   Compute the Collatz cycle length using memoization.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   30 minutes
Date:       11/14/2022
Questions:

    1. What is stored in the table passed to cycle_length()?

        ????

    2. How is table used in cycle_length() to implement memoization?

        ????

    3. What number between 100 and 1000 (inclusive) has the longest cycle
    length?

        ????
'''

from table import Map

import sys

# Functions

def cycle_length(n, table):
    ''' Return the collatz cycle length.

    >>> cycle_length(22, Map())
    16

    >>> cycle_length(58, Map())
    20

    >>> cycle_length(71, Map())
    103

    >>> cycle_length(1337, Map())
    45
    '''
    pass

# Main Execution

def main(stream=sys.stdin):
    ''' For each number in standard input, compute the cycle length, and print
    it out.

    >>> import io
    >>> main(io.StringIO('22\\n58\\n71\\n1337\\n'))
    Cycle Length of 22: 16
    Cycle Length of 58: 20
    Cycle Length of 71: 103
    Cycle Length of 1337: 45
    '''
    pass

if __name__ == '__main__':
    main()
