#!/usr/bin/python3

"""
Write a function that accepts a sequence (a list for example) and returns a new iterable (anything you can loop over) with adjacent duplicate values removed.
"""

def compact(seq):
    compacted = []
    last = None
    for item in seq:
        if item != last:
            compacted.append(item)
        last = item
