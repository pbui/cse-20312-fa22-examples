#!/usr/bin/env python3

''' bicolorable.py

Example of using traversal algorithm to solve graph problems.
'''

import collections
import sys

# Constants

BLUE = 0
RED  = 1

# Read Graph

def read_graph(stream=sys.stdin):
    ''' Construct adjacency list '''
    n, m = map(int, stream.readline().split())

    if not n or not m:
        return None

    graph = collections.defaultdict(list)

    for _ in range(m):
        source, target = map(int, stream.readline().split())
        graph[source].append(target)
        graph[target].append(source)

    return graph

# Determine if Bicolorable

def is_bicolorable(graph):
    ''' Determines if graph is bicolorable by walking it recursively. '''
    return walk(graph, min(graph), BLUE, {})

def walk(graph, start, color, visited):
    ''' Iteratively walk graph and verifying that the node has the appropriate
    color. '''
    # Establish frontier with initial node and color
    frontier = [(start, color)]

    # While there are still nodes in the frontier...
    while frontier:
        # Pop one node from frontier
        vertex, color = frontier.pop()

        # Check if it has been visited
        if vertex in visited:
            if color != visited[vertex]:
                return False
            continue

        # Mark that it has been visited
        visited[vertex] = color

        # Add neighbors to frontier
        for neighbor in graph[vertex]:
            frontier.append((neighbor, (color + 1) % 2))

    return True

def walk_r(graph, vertex, color, visited):
    ''' Recursively walk graph and verifying that the node has the appropriate
    color. '''

    # We have already visited this node, so verify we still have the same
    # color.
    if vertex in visited:
        return visited[vertex] == color

    # Visit each neighbor recursively with the alternate color and check that
    # they are colorable.
    for neighbor in graph[vertex]:
        # Make sure we store the color when we recurse.
        if not walk_r(graph, neighbor, (color + 1) % 2, visited | {vertex: color}):
            return False

    return True

# Main execution

def main(stream=sys.stdin):
    while graph := read_graph():
        if is_bicolorable(graph):
            print('BICOLORABLE')
        else:
            print('NOT BICOLORABLE')

if __name__ == '__main__':
    main()
