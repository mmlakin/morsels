#!/usr/bin/env python3

"""

 format_fixed_width.py

Write a function format_fixed_width() that accepts rows of columns (as
 a list of lists) and returns a fixed-width formatted string representing
 the given rows.
"""


def format_fixed_width(columns_list, *, padding=2, widths=None, alignments=None):
    output_list = ["" for _ in range(len(columns_list))]
    slice_index = 0
    for item_slice in [_ for _ in zip(*columns_list)]:
        index = 0

        if widths is not None:
            width = widths[slice_index] + padding
        else:
            width = len(max(item_slice, key=len)) + padding

        if alignments is not None and alignments[slice_index] == "R":
            alignment = "R"
        else:
            alignment = "L"

        for item in item_slice:
            print(f"[]{item.rjust(width)}]")
            if alignment == "L":
                output_list[index] += item.ljust(width)
            else:
                output_list[index] += item.rjust(width)
            # output_list[index] += (
            #     item.ljust(width) if alignment == "L" else item.rjust(width)
            # )
            index += 1
        slice_index += 1
    # print(output_list)
    output_string = "\n".join([line.rstrip() for line in output_list])
    print(output_string)
    return output_string
