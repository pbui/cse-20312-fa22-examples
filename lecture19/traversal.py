#!/usr/bin/env python3

''' traversal.py

This demonstrates traversing a tree using DFS and BFS.
'''

# Classes

from dataclasses import dataclass
from collections import deque

@dataclass
class Node:
    value:  str
    left:   'Node' = None
    right:  'Node' = None

# Functions

def dfs(root):
    ''' Traverse binary tree in depth-first order '''
    if not root: return                         # Base case: No Node

    dfs(root.left)                              # Recursive: Visit left branch
    print(root.value)                           # Visit current
    dfs(root.right)                             # Recursive: Visit right branch

def bfs(root):
    ''' Traverse binary tree in breadth-first order '''
    queue = deque([root])                       # Queue of nodes to visit

    while queue:
        node = queue.popleft()                  # Remove next node to visit
        print(node.value)                       # Visit node

        if node.left:  queue.append(node.left)  # Add left child
        if node.right: queue.append(node.right) # Add right child

# Main Execution

def main():
    tree = Node('B', Node('I', Node('A'), Node('R')), Node('N', Node('Y')))

    dfs(tree)
    print()
    bfs(tree)

if __name__ == '__main__':
    main()
