#!/usr/bin/env python3

'''
Title:      cups.py
Abstract:   Determine the minimum amount of time require to fill all cups of water.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   30 minutes
Date:       10/31/2022
Questiones:

    1. What is the worst-case time complexity of fill_cups()?

        ????

    2. What is the worst-case space complexity of fill_cups()?

        ????

    3. Why is this considered a greedy approach?

        ????
'''

import sys

from priority_queue import PriorityQueue

# Functions

def fill_cups(cups):
    ''' Return minimum number of seconds required to fill all cups of water.

    Use a greedy algorithm by attempting to fill two types of cups at a time
    until there is only one remaining type.
    >>> fill_cups([1, 4, 2])
    4

    >>> fill_cups([5, 4, 4])
    7

    >>> fill_cups([5, 0, 0])
    5
    '''
    pass

# Main Execution

def main(stream=sys.stdin):
    ''' For each line of cups, determine the minimum number of seconds required
    to fill all cups of water.

    >>> import io
    >>> main(io.StringIO('1 4 2\\n5 4 4\\n5 0 0\\n'))
    4
    7
    5
    '''
    pass

if __name__ == '__main__':
    main()
