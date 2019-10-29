#!/usr/bin/env python3

"""
Write a function that accepts a sequence (a list for example)
and returns a new iterable (anything you can loop over)
with adjacent duplicate values removed.
"""

from itertools import groupby
def compact(seq):
    for item,_ in groupby(seq):
        yield item

def icompact(seq):
    """Use object() as a unique default value so seq can include values like None"""
    last = object()
    for item in seq:
        if item != last:
            yield item
        last = item

def lcompact(seq):
    compacted = []
    last = object()
    for item in seq:
        if item != last:
            compacted.append(item)
        last = item
    return compacted

