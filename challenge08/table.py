#!/usr/bin/env python3

'''
Title:      table.py
Abstract:   Implement a Map class using a hash table with separate chaining.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   30 minutes
Date:       11/14/2022
Questions:

    1. What is worst-case time complexity of Map.insert()?

        ????

    2. What is worst-case time complexity of Map.search()?

        ????

    3. What is the load factor of a hash table?

        ????

    4. To ensure the time complexities stated above, what must the hash table
    do internally when the load factor reaches a certain threshold?

        ????
'''

from dataclasses import dataclass

# Constants

FNV_OFFSET_BASIS = 14695981039346656037
FNV_PRIME        = 1099511628211

# Classes

@dataclass
class Pair:
    ''' Pair with string key and integer value. '''
    pass

class Map:
    ''' Map Implementation based on a hash table. '''

    LOAD_FACTOR = 1.5

    def __init__(self, nbuckets=8):
        ''' Initialize empty Map.

        >>> m = Map()
        >>> len(m.buckets)
        8

        >>> m = Map(4)
        >>> m.buckets
        [[], [], [], []]
        >>> m.size
        0
        '''
        pass

    def insert(self, key, value):
        ''' Insert key, value pair into Map.  If key is already in Map, then
        update value.

        >>> m = Map()
        >>> m.insert('D', 0); m.buckets[3]
        [Pair(key='D', value=0)]
        >>> m.size
        1

        >>> m.insert('F', 1); m.buckets[1]
        [Pair(key='F', value=1)]
        >>> m.size
        2

        >>> m.insert('H', 2); m.buckets[7]
        [Pair(key='H', value=2)]
        >>> m.size
        3

        >>> m.insert('C', 3); m.buckets[2]
        [Pair(key='C', value=3)]
        >>> m.size
        4

        >>> m.insert('A', 4); m.buckets[4]
        [Pair(key='A', value=4)]
        >>> m.size
        5

        >>> m.insert('A', 6); m.buckets[4]
        [Pair(key='A', value=6)]
        >>> m.size
        5
        '''
        pass

    def lookup(self, key):
        ''' Lookup key in Map and return associated value (None if missing).

        >>> m = Map()
        >>> d = [('sbn', 574), ('eau', 715), ('sna', 714), ('nyc', 646)]
        >>> for k, v in d: m.insert(k, v)
        >>> all(m.lookup(k) == v for k, v in d)
        True

        >>> m.lookup('stl')
        '''
        pass

    def resize(self):
        ''' Resize the hash table by creating a new buckets array that is twice
        as large, rehashing the existing Pairs into the new buckets array, and
        then reassigning the internal buckets array to this new array.

        >>> m = Map(2)
        >>> d = [('sbn', 574), ('eau', 715), ('sna', 714), ('nyc', 646), ('stl', 314)]
        >>> for k, v in d: m.insert(k, v)
        >>> len(m.buckets)
        4
        >>> all(m.lookup(k) == v for k, v in d)
        True
        '''
        pass

    @staticmethod
    def hash(d):
        ''' Compute the FNV-1a hash on the string or int d.

        >>> Map.hash('notre')
        4751529075592153558511737267927

        >>> Map.hash('dame')
        16047809754340873646920371502188

        >>> Map.hash(574)
        10222938680436398074917206614173
        '''
        if isinstance(d, str):
            d = d.encode()

        pass
