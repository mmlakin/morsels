#!/usr/bin/env python3

"""
tail() - Return the last n items of given iterable.
"""

from collections import deque

def tail(iterable, num):
    """Return last num items of iterable"""
    if num <= 0:
        return []
    return list(deque(iterable, maxlen=num))
