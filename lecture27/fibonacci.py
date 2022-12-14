#!/usr/bin/env python3

''' fibonacci.py

Use memoization to speedup computing the nth Fibonacci number:

    Fibonacci(n) = Fibonacci(n - 1) + Fibonacci(n - 2)
'''

import sys

# Functions

def fibonacci(n, cache={}):
    ''' Compute the nth number in the Fibonacci sequence.

    >>> fibonacci(1)
    1

    >>> fibonacci(5)
    5
    
    >>> fibonacci(10)
    55
    '''

    # Base cases
    if n == 0:
        return 0
    elif n <= 2:
        return 1

    # Recursive step
    '''
    return fibonacci(n - 1) + fibonacci(n - 2)
    '''

    # Recursive step: memoized
    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]

# Main Execution

def main():
    for i in map(int, sys.stdin):
        print('fibonacci({}) = {}'.format(i, fibonacci(i)))

if __name__ == '__main__':
    main()
