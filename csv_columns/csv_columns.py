#!/usr/bin/env python3
"""
csv_columns.py
    accepts a file object and returns a dictionary mapping CSV headers to
    column data for each header.
"""
import csv
import sys
import collections
def csv_columns(input_file_obj, *, headers=None, missing=None) -> dict:
    """ Takes a file and returns a dict mapping headers to data"""
    csv_file = csv.reader(input_file_obj)
    csv_dict = collections.OrderedDict()
    if headers:
        csv_headers = headers
    else:
        csv_headers = next(csv_file)
    for row in csv_file:
        for _ in range(len(csv_headers) - len(row)):
            row.append(missing)
        for header, value in zip(csv_headers, row):
            if header not in csv_dict:
                csv_dict[header] = []
            csv_dict[header].append(value)
    return csv_dict

def main(args):
    """ Main function """
    csv_columns(args)

if __name__ == "__main__":
    main(sys.argv[1])
