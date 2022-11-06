#!/usr/bin/env python3

''' Cheatsheet of common set operations in Python. '''

# Empty set
set1 = set()                

# Initialized set
set2 = set(['a', 'b', 'a'])

# Print length and contents
print(len(set2), set2)

# Search for value in set
print('a' in set2)

# Insert into set
set1.add('a')
set1.add('b')

# Iterate through values in set
for value in set1:
    print(value)

# Remove items from set
set1.remove('a')
set1.remove('b')

print(set1)
