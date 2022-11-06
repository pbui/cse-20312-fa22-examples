#!/usr/bin/env python3

''' Cheatsheet of common set operations in Python. '''

set1 = set()                # Empty set
set2 = set(['a', 'b', 'a']) # Set from list

# Print length and contents
print(len(set1), set1)
print(len(set2), set2)

# Insert into set
set1.add('a')
set1.add('b')

# Iterate through set
for value in set1:
    print(value)

# Remove items from set
set1.remove('a')
set1.remove('b')

print(set1)
