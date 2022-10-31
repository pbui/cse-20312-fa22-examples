#!/usr/bin/env python3

'''
Title:      tree.py
Abstract:   Implement a binary tree read and walk functions.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   25 minutes
Date:       11/01/2022
Questions:

    1. What is the worst-case time complexity of tree_read()?

        ????

    2. What is the worst-case time complexity of tree_walk()?

        ????

    3. In tree_walk(), how did you modify BFS to print all the nodes on one
    comma separated line?

        ????

    4. In tree_walk(), how did you remove any trailing invalid nodes from your
    output?

        ????
'''

from dataclasses import dataclass
from collections import deque

# Classes

@dataclass
class Node:
    pass

# Functions

def tree_read(array, index=0):
    ''' Return a node-based tree from the given array of values in BFS format.

    >>> tree_read([1, 2, 3])
    Node(value=1, left=Node(value=2, left=None, right=None), right=Node(value=3, left=None, right=None))

    >>> tree_read([1, 2, 3, 4, 0, 0, 6])
    Node(value=1, left=Node(value=2, left=Node(value=4, left=None, right=None), right=None), right=Node(value=3, left=None, right=Node(value=6, left=None, right=None)))
    '''
    pass

def tree_walk(root):
    ''' Print out the tree in level-by-level order with each level on the same
    line.

    >>> tree_walk(tree_read([1, 2, 3]))
    1, 2, 3
    >>> tree_walk(tree_read([1, 2, 3, 4, 0, 0, 6]))
    1, 2, 3, 4, 0, 0, 6
    '''
    pass
