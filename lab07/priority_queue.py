#!/usr/bin/env python3

'''
Title:      priority_queue.py
Abstract:   Implement a priority queue using an array-based binary tree.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   25 minutes
Date:       10/25/2022
Questions:

    1. While performing a BFS, how do you know if node is valid or not?

        ????

    2. What is the worst-case time complexity of PriorityQueue.pop()?

        ????

    3. What is the worst-case space complexity of PriorityQueue.pop()?

        ????
'''

from collections import deque

# Classes

class PriorityQueue:
    ''' Simple priority queue using an array-based binary tree. '''

    def __init__(self, tree):
        ''' Initialize internal binary tree.

        >>> pq = PriorityQueue([4, 6, 6, 3, 7]); pq.tree
        [4, 6, 6, 3, 7]
        '''
        pass

    def pop(self):
        ''' Return the largest value in priority queue.

        Walk tree using BFS to find largest value, place 0 in its place, and
        then return largest value.

        >>> pq = PriorityQueue([4, 6, 6, 3, 7])
        >>> [pq.pop(), pq.pop(), pq.pop(), pq.pop(), pq.pop()]
        [7, 6, 6, 4, 3]
        >>> pq.tree
        [0, 0, 0, 0, 0]
        '''
        pass

# Functions

def left_child(index):
    ''' Return index of left child.

    >>> left_child(0)
    1

    >>> left_child(1)
    3
    '''
    pass

def right_child(index):
    ''' Return index of right child.

    >>> right_child(0)
    2

    >>> right_child(1)
    4
    '''
    pass
