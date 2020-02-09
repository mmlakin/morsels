#!/usr/bin/env python3
"""
csv_columns.py
    accepts a file object and returns a dictionary mapping CSV headers to
    column data for each header.
"""
import csv
import itertools
def csv_columns(input_file_obj, *, headers=None, missing=None) -> dict:
    """ Takes a file and returns a dict mapping headers to data"""
    csv_file = csv.reader(input_file_obj)
    if headers:
        csv_headers = headers
    else:
        csv_headers = next(csv_file)
    return {
        header: value
        for header, *value in itertools.zip_longest(csv_headers, *csv_file, fillvalue=missing)
    }
