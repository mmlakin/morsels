#!/usr/bin/env python3

"""
 tags_equal.py

 Take two strings containing opening HTML tags and return True if they have
 the same attributes with the same values.
"""


def clean_tag(tag: str) -> list:
    """ Cleans a tag and returns a dict of tag keys and values, respecting the
        first value set for a key """

    # Remove markup symbols
    markup = "<", ">"
    for symbol in markup:
        tag = tag.replace(symbol, "")

    tag = tag.upper()
    tag = tag.split(" ")

    tagdict = dict()
    quotedstringkey = None
    quotes = "'", '"'
    for item in tag:
        if quotedstringkey is not None:
            previouskey = quotedstringkey
            if item[-1] in quotes:
                quotedstringkey = None
            for quote in quotes:
                item = item.replace(quote, "")
            tagdict[previouskey] += f" {item}"
            continue

        item = item.split("=")
        key = item[0]
        if key not in tagdict.keys():
            value = item[1] if len(item) > 1 else ""
            if value != "":
                if value[0] in quotes and value[-1] not in quotes:
                    quotedstringkey = key
                for quote in quotes:
                    value = value.replace(quote, "")
            tagdict[key] = value

    return tagdict


def tags_equal(tag1: str, tag2: str) -> bool:
    return clean_tag(tag1) == clean_tag(tag2)
