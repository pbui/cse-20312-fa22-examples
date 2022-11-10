#!/usr/bin/env python3

''' table.py

A simple Set class implemented as a hash table.
'''

# Classes

class Set:

    def __init__(self, nbuckets=8):
        ''' Initialize set. 

        >>> s = Set()
        >>> len(s.buckets)
        8
        '''
        self.buckets = [0 for _ in range(nbuckets)]
    
    def insert(self, value):
        ''' Insert value into set.

        >>> s = Set()
        >>> d = [4, 6, 6, 3, 7]
        >>> for v in d: s.insert(v)
        >>> all(v in s.buckets for v in d)
        True
        '''
        bucket = hash(value) % len(self.buckets)
        self.buckets[bucket] = value

    def search(self, value):
        ''' Return whether or not value is in set.

        >>> s = Set()
        >>> d = [4, 6, 6, 3, 7]
        >>> for v in d: s.insert(v)
        >>> all(s.search(v) for v in d)
        True
        '''
        bucket = hash(value) % len(self.buckets)
        return self.buckets[bucket] == value
