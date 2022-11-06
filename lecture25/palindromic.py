#!/usr/bin/env python3

''' palindromic

Demonstrate how to use a set or dict to determine if a word has a palindromic
permutation.
'''

import sys

# Functions

def is_palindromic_dict(word):
    ''' Return whether or not a word has a palindromic permutation.

    >>> is_palindromic_dict('anan')
    True
    
    >>> is_palindromic_dict('abad')
    False

    >>> is_palindromic_dict('cattaco')
    True

    >>> is_palindromic_dict('audric')
    False
    
    >>> is_palindromic_dict('carcare')
    True
    '''
    counts = {}     # Table of occurrences (number of times each letter appears)
    
    '''
    # Count each letter: Check first
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter]  = 1

    # Count each letter: Try / Except 
    for letter in word:
        try:
            counts[letter] += 1
        except KeyError:
            counts[letter]  = 1
    '''
    
    # Count each letter: Using get method for default value
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1

    # Count number of odd counts
    odds = 0
    for count in counts.values():
        if count % 2:
            odds += 1

    return odds <= 1

def is_palindromic_set(word):
    ''' Return whether or not a word has a palindromic permutation.

    >>> is_palindromic_set('anan')
    True
    
    >>> is_palindromic_set('abad')
    False

    >>> is_palindromic_set('cattaco')
    True

    >>> is_palindromic_set('audric')
    False
    
    >>> is_palindromic_set('carcare')
    True
    '''
    seen = set()                # Track whether or not we have seen a letter

    for letter in word:
        if letter in seen:      # Remove letter if seen before
            seen.remove(letter)
        else:
            seen.add(letter)    # Add if letter not seen before

    return len(seen) <= 1       # Palindromic if we only have at most 1 remaining letter

# Main Execution

def main(stream=sys.stdin):
    ''' For each word in the stream, determine if it has a palindromic permutation.

    >>> import io
    >>> main(io.StringIO('anan\\nabad\\ncattaco\\n'))
    anan has a palindromic permutation
    abad doesn't have a palindromic permutation
    cattaco has a palindromic permutation
    '''

    for word in stream:
        word = word.strip()
        if is_palindromic_set(word):
            print(f'{word} has a palindromic permutation')
        else:
            print(f"{word} doesn't have a palindromic permutation")

if __name__ == '__main__':
    main()
