#!/usr/bin/env python3

"""

 format_fixed_width.py

Write a function format_fixed_width() that accepts rows of columns (as
 a list of lists) and returns a fixed-width formatted string representing
 the given rows.
"""


def format_fixed_width(columns_list, *, padding=2):
    output_list = ["" for _ in range(len(columns_list))]
    for item_slice in [_ for _ in zip(*columns_list)]:
        index = 0
        width = len(max(item_slice, key=len)) + padding
        for item in item_slice:
            # print(f"[]{item.ljust(width)}]")
            output_list[index] += item.ljust(width)
            index += 1
    # print(output_list)
    return "\n".join([line.rstrip() for line in output_list])
