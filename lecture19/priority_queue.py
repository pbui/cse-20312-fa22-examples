#/usr/bin/env python3

''' Priority Queue (sort).

A simple Priority Queue class implemented by sorting the data internally.
'''

# Classes

class PriorityQueue:

    def __init__(self, data=None):   # Constructor
        ''' Initialize the internal data.

        >>> pq = PriorityQueue(); pq.data
        []

        >>> pq = PriorityQueue([3, 1, 4]); pq.data[0]
        1
        '''
        self.data = data if data else []
        self.data.sort()

    def push(self, item):
        ''' Add item to Priority Queue.

        >>> pq = PriorityQueue(); pq.push(3); pq.data[-1]
        3

        >>> pq.push(1); pq.data[-1]
        3

        >>> pq.push(4); pq.data[-1]
        4
        '''
        self.data.append(item)
        self.data.sort()

    def pop(self):
        ''' Remove and return largest element from the Priority Queue.
        >>> pq = PriorityQueue([3, 1 ,4]); pq.pop()
        4

        >>> pq.pop()
        3

        >>> pq.pop()
        1
        '''
        return self.data.pop()

    def empty(self):
        ''' Return whether or not the Priority Queue is empty.

        >>> pq = PriorityQueue(); pq.empty()
        True

        >>> pq = PriorityQueue([3, 1, 4]); pq.empty()
        False
        '''
        return not self.data
