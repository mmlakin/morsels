#!/usr/bin/env python3

"""
 chunked.py
 Accepts a sequence and a number n and returns one list-of-lists containing
 lists of size n.
"""

nulobj = object()


def chunked(sequence, number, *, fill=nulobj) -> list:
    newlist = []
    for item in sequence:
        newlist.append(item)
        if len(newlist) >= number:
            yield newlist
            newlist = []
    if len(newlist) > 0:
        if fill is not nulobj:
            for _ in range(number - len(newlist)):
                newlist.append(fill)
        yield newlist
