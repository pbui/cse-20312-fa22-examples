#!/usr/bin/env python3

'''
Title:      invert.py
Abstract:   Invert binary tree.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   25 minutes
Date:       11/01/2022
Questions:

    1. What is the worst-case time complexity of tree_invert()?

        ????

    2. How do you swap two values in Python without a temporary value?

        ????
'''

import sys

# Functions

def tree_invert(node):
    ''' Invert tree in-place using divide and conquere.

    >>> tree_walk(tree_invert(tree_read([1, 2, 3])))
    1, 3, 2

    >>> tree_walk(tree_invert(tree_read([1, 2, 3, 4, 0, 0, 6])))
    1, 3, 2, 6, 0, 0, 4
    '''
    pass

# Main Execution

def main(stream=sys.stdin):
    ''' For each line, read in the tree in BFS format, print it, invert it, and
    then print it again.

    >>> import io
    >>> main(io.StringIO('1 2 3\\n1 2 3 4 0 0 6\\n'))
    1, 2, 3
    1, 3, 2
    1, 2, 3, 4, 0, 0, 6
    1, 3, 2, 6, 0, 0, 4
    '''
    pass

if __name__ == '__main__':
    main()
