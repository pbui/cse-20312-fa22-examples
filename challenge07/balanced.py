#!/usr/bin/env python3

'''
Title:      balanced.py
Abstract:   Determine wether or not a binary tree is balanced.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   30 minutes
Date:       11/07/2022
Questions:

    1. What is the worst-case time complexity of is_balanced()?

        ????

    2. What information does is_balanced() return?

        ????
'''

import sys

# Functions

def is_balanced(array, index=0):
    ''' Determine whether or not a binary tree is balanced.

    A binary tree is balanced if:

    1. Left and right sub-trees are balanced.
    2. Difference between heights of left and right sub-trees is no more than 1.

    >>> is_balanced([5, 3, 6])
    (True, 2)

    >>> is_balanced([5, 3, 6, 4])
    (True, 3)

    >>> is_balanced([5, 3, 0, 4])
    (False, 3)

    >>> is_balanced([5, 3, 4, 0, 1])
    (True, 3)

    >>> is_balanced([5, 3, 4, 0, 1, 0, 0, 0, 0, 2])
    (False, 4)
    '''
    pass

# Main Execution

def main(stream=sys.stdin):
    ''' For each line with a tree given in BFS format, output whether or not it
    is balanced.

    >>> import io
    >>> main(io.StringIO('5 3 6\\n5 3 6 4\\n5 3 0 4\\n'))
    Balanced
    Balanced
    Not Balanced
    '''
    pass

if __name__ == '__main__':
    main()
