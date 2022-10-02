"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    items_str = list(map(str, items))
          ##Changes each element to a string
    for i in items_str:
        count = 0
        count = items_str.count(i)

        if i in frequencies.keys():
            pass ##Checks if key is already exists
        else:
            frequencies[i] = count
    return frequencies
