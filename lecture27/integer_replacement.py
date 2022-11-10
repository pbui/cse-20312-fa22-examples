#!/usr/bin/env python3

''' integer_replacement.py

https://leetcode.com/problems/integer-replacement/

Given a positive integer n, you can apply one of the following operations:

    1. If n is even, replace n with n / 2.
    2. If n is odd, replace n with either n + 1 or n - 1.

Return the minimum number of operations needed for n to become 1.
'''

import sys

# Functions

def count_operations(n):
    ''' Return number of operations needed for n to become 1.

    >>> count_operations(8)
    3

    >>> count_operations(7)
    4

    >>> count_operations(4)
    2

    >>> count_operations(1234)
    14
    '''
    # Base case: Found 1
    if n == 1:
        return 0

    # Recursive case: Use Rules
    if n % 2:   # Odd
        return min(count_operations(n - 1), count_operations(n + 1)) + 1
    else:       # Even
        return count_operations(n // 2) + 1

def count_operations_cached(n, cache={}):
    ''' Return number of operations needed for n to become 1.

    Use a cache to implement memoization.

    >>> count_operations_cached(8)
    3

    >>> count_operations_cached(7)
    4

    >>> count_operations_cached(4)
    2

    >>> count_operations_cached(1234)
    14
    '''

    # Base case: Found 1
    if n == 1:
        return 0

    # Recursive case: Use Rules
    if n not in cache:
        if n % 2:   # Odd
            cache[n] = min(
                count_operations_cached(n - 1, cache),
                count_operations_cached(n + 1, cache)
            ) + 1
        else:       # Even
            cache[n] = count_operations_cached(n // 2, cache) + 1

    return cache[n]

# Main Execution

def main(stream=sys.stdin, use_cache=False):
    ''' For each integer, count the number of operations required for the
    integer to become 1.

    Use a cache if use_cache is True.

    >>> import io
    >>> main(io.StringIO('8\\n7\\n4\\n'))
    3
    4
    2
    '''
    cache = {}

    for line in stream:
        n = int(line)
        if use_cache:
            print(count_operations_cached(n, cache))
        else:
            print(count_operations(n))

if __name__ == '__main__':
    main(use_cache=len(sys.argv) > 1 and sys.argv[1] == '-c')
