#!/usr/bin/env python3

''' table_sc.py

A simple Set class implemented as a hash table with separate chaining.
'''

# Classes

class Set:

    def __init__(self, nbuckets=8):
        ''' Initialize set. 

        >>> s = Set()
        >>> len(s.buckets)
        8
        '''
        self.buckets = [[] for _ in range(nbuckets)]
    
    def insert(self, value):
        ''' Insert value into set.

        >>> s = Set()
        >>> d = [4, 6, 6, 3, 7]
        >>> for v in d: s.insert(v)
        >>> all(any(v in b for b in s.buckets) for v in d)
        True
        '''
        bucket = hash(value) % len(self.buckets)

        if not value in self.buckets[bucket]:
            self.buckets[bucket].append(value)

    def search(self, value):
        ''' Return whether or not value is in set.

        >>> s = Set()
        >>> d = [4, 6, 6, 3, 7]
        >>> for v in d: s.insert(v)
        >>> all(s.search(v) for v in d)
        True
        '''
        bucket = hash(value) % len(self.buckets)
        return value in self.buckets[bucket]
