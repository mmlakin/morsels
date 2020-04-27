#!/usr/bin/env python3

"""

 format_fixed_width.py

Write a function format_fixed_width() that accepts rows of columns (as
 a list of lists) and returns a fixed-width formatted string representing
 the given rows.
"""


def format_fixed_width(columns_list):
    output_string = ""
    padding = 2
    width = 0
    largest_column = 0
    for column in columns_list:
        column_size = sum(len(item) for item in column)
        if column_size > largest_column:
            largest_column = column_size
    width = largest_column + padding
    for column in columns_list:
        column_size = sum(len(item) for item in column)
        column_padding = (width - column_size) * " "
        output_string += f"{column[0]}{column_padding}{column[1:]}\n"
    return output_string
