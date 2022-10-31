#!/usr/bin/env python3

'''
Title:      set.py
Abstract:   Implement a Set using a binary search tree.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   30 minutes
Date:       10/31/2022
Questions:

    1. What is the average time complexity insert()?

        ????
    
    2. What is the worst-case time complexity insert()?

        ????

    3. What is the base case for the _insert() and _search() methods?

        ???
'''

from dataclasses import dataclass

# Classes

@dataclass
class Node:
    ''' Simple Node with string key and int value. '''
    pass

class Set:
    ''' Simple Set Implementation based on a binary search tree. '''

    def __init__(self):
        ''' Initialize empty set.

        >>> s = Set(); not s.root
        True
        '''
        pass

    def insert(self, value):
        ''' Insert value pair into set.

        Test tree:

                 5
               /   \
              4     7
             /       \
            1         9

        >>> s = Set()
        >>> s.insert(5); s.root.value
        5

        >>> s.insert(7); s.root.right.value
        7

        >>> s.insert(4); s.root.left.value
        4

        >>> s.insert(9); s.root.right.right.value
        9

        >>> s.insert(1); s.root.left.left.value
        1
        '''
        pass
    
    def _insert(self, node, value):
        ''' Insert value into set (recursive). '''
        pass

    def search(self, value):
        ''' Return whether or not value is in set.

        >>> s = Set()
        >>> for n in [5, 7, 4, 9, 1]: s.insert(n)
        >>> all(s.search(n) for n in [5, 7, 4, 9, 1])
        True

        >>> any(s.search(n) for n in [0, 3, 8, 10])
        False
        '''
        pass
    
    def _search(self, node, value):
        ''' Return whether or not value is in set (recursive). '''
        pass
