#!/usr/bin/env python3

'''
Title:      sim_city.py
Abstract:   Compute the minimum spanning tree of points in a city map.
Author:     Peter Bui
Email:      pbui@nd.edu
Estimate:   30 minutes
Date:       12/7/2022
Questions:

    1. What is the average time complexity of build_graph?

        ????

    2. What is the average time complexity of compute_mst?

        ????

    3. What is the average space complexity of compute_mst?

        ????

    4. Does the total cost of the minimum spanning tree change if we use
    different starting vertices isfor compute_mst?  Experiment and then
    explain.

        ????
'''

import collections
import heapq
import io
import math
import requests
import sys

# Constants

POINTS_URL  = 'https://yld.me/raw/jpIx'
POINTS_TEXT = requests.get(POINTS_URL).text

# Read Points

def read_points(stream=sys.stdin):
    ''' Read points from stream.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> read_points(points_stream)
    [(0, 1.0, 1.0), (1, 2.0, 2.0), (2, 2.0, 4.0)]

    >>> read_points(points_stream)
    [(0, 1.0, 1.0), (1, 2.0, 2.0), (2, 1.0, 2.0), (3, 2.0, 1.0)]

    >>> read_points(points_stream)
    [(0, 0.0, 1.0), (1, 2.0, 3.0), (2, 4.0, 1.0), (3, 1.0, 2.0), (4, 5.0, 2.0)]
    '''
    pass

# Build Graph

def build_graph(points):
    ''' Build adjacency list from list of points.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 1.4142135623730951, 2: 3.1622776601683795}, 1: {0: 1.4142135623730951, 1: 0.0, 2: 2.0}, 2: {0: 3.1622776601683795, 1: 2.0, 2: 0.0}})

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 1.4142135623730951, 2: 1.0, 3: 1.0}, 1: {0: 1.4142135623730951, 1: 0.0, 2: 1.0, 3: 1.0}, 2: {0: 1.0, 1: 1.0, 2: 0.0, 3: 1.4142135623730951}, 3: {0: 1.0, 1: 1.0, 2: 1.4142135623730951, 3: 0.0}})

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 2.8284271247461903, 2: 4.0, 3: 1.4142135623730951, 4: 5.0990195135927845}, 1: {0: 2.8284271247461903, 1: 0.0, 2: 2.8284271247461903, 3: 1.4142135623730951, 4: 3.1622776601683795}, 2: {0: 4.0, 1: 2.8284271247461903, 2: 0.0, 3: 3.1622776601683795, 4: 1.4142135623730951}, 3: {0: 1.4142135623730951, 1: 1.4142135623730951, 2: 3.1622776601683795, 3: 0.0, 4: 4.0}, 4: {0: 5.0990195135927845, 1: 3.1622776601683795, 2: 1.4142135623730951, 3: 4.0, 4: 0.0}})
    '''
    pass

# Compute MST

def compute_mst(graph, start):
    ''' Compute minimum spanning tree.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 1: 0, 2: 1}

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 2: 0, 1: 2, 3: 0}

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 3: 0, 1: 3, 2: 1, 4: 2}
    '''
    pass

# Main Execution

def main(stream=sys.stdin):
    ''' For each set of points, build the graph, compute the MST, and then
    print out the total cost.

    >>> main(io.StringIO(POINTS_TEXT))
    Graph 1: 3.41
    Graph 2: 3.00
    Graph 3: 7.07
    Graph 4: 12.73
    Graph 5: 27.08
    '''
    pass

if __name__ == '__main__':
    main()
