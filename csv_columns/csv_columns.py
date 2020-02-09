#!/usr/bin/env python3
"""
csv_columns.py
    accepts a file object and returns a dictionary mapping CSV headers to
    column data for each header.
"""
import csv
from itertools import zip_longest
def csv_columns(input_file_obj, *, headers=None, missing=None) -> dict:
    """ Takes a file and returns a dict mapping headers to data"""
    csv_file = csv.reader(input_file_obj)
    if headers is None:
        headers = next(csv_file)
    columns = zip_longest(*csv_file, fillvalue=missing)
    return {
        header: list(column)
        for header, column in zip(headers, columns)
    }
