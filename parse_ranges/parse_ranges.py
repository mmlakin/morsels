#!/usr/bin/env python3

import re

re_split = r',\s*'
re_single = r'^\d+$'
re_range = r'^(\d+)\-(\d+)$'
re_arrow = r'^(\d+)\-\>.*$'

def parse_ranges(str_) -> iter:
    """  Takes a string of numbers and ranges, like:
        "1,2-2,3-6,8,11-13"
        and yields each integer
    """
    items = re.split(',\s*', str_)

    for item in items:
        singlelist = re.findall(re_single, item)
        rangelist = re.findall(re_range, item)
        arrowlist = re.findall(re_arrow, item)

        for digit in singlelist + arrowlist:
            digit = int(digit)
            yield digit

        for start,stop in rangelist:
            start,stop = int(start), int(stop)
            stop += 1
            yield from range(start,stop)

