#!/usr/bin/env python3

''' Cheatsheet of common dict operations in Python. '''

# Empty dict
dict1 = {}

# Initialized dictionary
dict2 = {'a': 1, 'b': 2}

# Print length and contents
print(len(dict2), dict2)

# Search for value in dict
print('a' in dict2)

# Insert into dict
dict2['c'] = 3

# Iterate through keys in dict
for key in dict2:
    print(key, dict2[key])

# Iterate through values in dict
for value in dict2.values():
    print(value)

# Iterate through pairs in dict
for key, value in dict2.items():
    print(key, value)

# Remove items from dict
del dict2['a']

print(dict2)
