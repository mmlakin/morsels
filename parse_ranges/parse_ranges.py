#!/usr/bin/env python3

"""
parse_ranges.py - Take string of ints and ranges and return iterator
"""
import re

RE_SPLIT = r',\s*'
RE_SINGLE = r'^\d+$'
RE_RANGE = r'^(\d+)\-(\d+)$'
RE_ARROW = r'^(\d+)\-\>.*$'

def parse_ranges(str_) -> iter:
    """  Takes a string of numbers and ranges, like:
        "1,2-2,3-6,8,11-13"
        and yields each integer
    """
    items = re.split(RE_SPLIT, str_)

    for item in items:
        singlelist = re.findall(RE_SINGLE, item)
        rangelist = re.findall(RE_RANGE, item)
        arrowlist = re.findall(RE_ARROW, item)

        for digit in singlelist + arrowlist:
            digit = int(digit)
            yield digit

        for start, stop in rangelist:
            start, stop = int(start), int(stop)
            stop += 1
            yield from range(start, stop)
