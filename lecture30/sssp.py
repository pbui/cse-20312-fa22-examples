#!/usr/bin/env python3

''' sssp.py

Example of Dijkstra's algorithm for single source shortest path.
'''

import collections
import heapq
import sys

# Build Graph

def read_graph():
    ''' Read in undirected graph '''
    graph = collections.defaultdict(dict)
    for line in sys.stdin:
        source, target, weight = line.split()
        graph[source][target] = int(weight)
        graph[target][source] = int(weight)
    return graph

# Compute SSSP

def compute_sssp(graph, start):
    ''' Use Dijkstra's Algorithm to compute the single-source shortest path '''
    frontier = []
    visited  = {}

    heapq.heappush(frontier, (0, start, start))

    while frontier:
        weight, source, target = heapq.heappop(frontier)

        if target in visited:
            continue

        visited[target] = source

        for neighbor, cost in graph[target].items():
            heapq.heappush(frontier, (weight + cost, target, neighbor))

    return visited

def reconstruct_path(graph, visited, source, target):
    ''' Reconstruct path from source to target '''
    path = []
    curr = target
    cost = 0

    while curr != source:
        path.append(curr)
        prev  = visited[curr]
        cost += graph[prev][curr]
        curr  = prev

    path.append(source)
    return reversed(path), cost

# Main Execution

def main():
    # Read Graph
    graph   = read_graph()

    # Compute SSSP
    start   = min(graph.keys())
    visited = compute_sssp(graph, start)

    # Reconstruct Path
    for target in list(graph.keys())[1:]:
        path, cost = reconstruct_path(graph, visited, start, target)
        print(f'{start} -> {target} = {cost}, {" ".join(path)}')

if __name__ == '__main__':
    main()
