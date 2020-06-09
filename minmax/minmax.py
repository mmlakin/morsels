#!/usr/bin/env python3
"""
 minmax.py

 Accepts a list and returns a tuple of the min and max values in that list.
"""


class minmax:
    def __init__(self, input_iter: iter, *, key=None):
        sorted_list = sorted(input_iter, key=key)
        if sorted_list == []:
            raise ValueError
        self.min = sorted_list[0]
        self.max = sorted_list[-1]

    def __iter__(self):
        yield self.min
        yield self.max
