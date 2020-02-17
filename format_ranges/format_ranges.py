#!/usr/bin/env python3
"""
 format_ranges.py

This week I'd like you to write a function format_ranges, that takes a list of numbers and returns a string that groups ranges of consecutive numbers together:

>>> format_ranges([1, 2, 3, 4, 5, 6, 7, 8])
'1-8'
>>> format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])
'1-3,5-8,10-11'

All runs of consecutive numbers will be collapsed into N-M ranges where N is the start of the consecutive range and M is the end.

This is sort of like the format that printers use for choosing which pages to print.

At first you can assume that all consecutive ranges of numbers will be at least 2 consecutive numbers long.

"""


def format_ranges(numlist):
    ordered_numlist = sorted(numlist)
    last_num = None
    consecutive = False
    for number in ordered_numlist:
        if last_num is None:
            output_string = str(number)
        elif number is last_num or number is last_num + 1:
            if consecutive is False:
                output_string += "-"
                consecutive = True
        else:
            if consecutive is True:
                output_string += str(last_num)
            output_string += f",{str(number)}"
            consecutive = False
        last_num = number
    if consecutive is True:
        output_string += str(last_num)
    return output_string
