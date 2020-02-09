#!/usr/bin/env python3
"""
csv_columns.py
    accepts a file object and returns a dictionary mapping CSV headers to
    column data for each header.
"""
import csv
import collections
import itertools
def csv_columns(input_file_obj, *, headers=None, missing=None) -> dict:
    """ Takes a file and returns a dict mapping headers to data"""
    csv_file = csv.reader(input_file_obj)
    csv_dict = collections.OrderedDict()
    if headers:
        csv_headers = headers
    else:
        csv_headers = next(csv_file)
    for row in csv_file:
        for header, value in itertools.zip_longest(csv_headers, row, fillvalue=missing):
            csv_dict.setdefault(header, []).append(value)
    return csv_dict
