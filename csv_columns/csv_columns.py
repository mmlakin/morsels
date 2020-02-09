#!/usr/bin/env python3
"""
csv_columns.py
    accepts a file object and returns a dictionary mapping CSV headers to
    column data for each header.
"""
import csv
from collections import defaultdict

def csv_columns(input_file_obj, *, headers=None, missing=None) -> dict:
    """Takes a file object and returns a dict mapping headers to values"""
    csv_file = csv.DictReader(input_file_obj, fieldnames=headers, restval=missing)
    csv_dict = defaultdict(list)
    for row in csv_file:
        for header, value in row.items():
            csv_dict[header].append(value)
    return csv_dict
