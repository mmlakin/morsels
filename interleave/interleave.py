#!/usr/bin/env python3
"""
interleave.py

Write a function that accepts two lists and returns a new iterable with each
of the given items "interleaved" (item 0 from iterable 1, then item 0 from
iterable 2, then item 1 from iterable 1, and so on).
"""


def interleave(list1: list, list2: list) -> iter:
    """Interleave items between the two supplied lists"""
    for item1, item2 in zip(list1, list2):
        yield item1
        yield item2
