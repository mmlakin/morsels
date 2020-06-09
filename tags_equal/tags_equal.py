#!/usr/bin/env python3

"""
 tags_equal.py

 Take two strings containing opening HTML tags and return True if they have
 the same attributes with the same values.
"""


def clean_tag(tag: str) -> list:
    """ Returns a tuple containing the tag name and a dict of the tag's keys
        and values, respecting the first value set for a key """
    tagdict = dict()
    quotedstringkey = None
    quotes = "'", '"'

    # Remove brackets around tag
    tag = tag[1:-1]

    tag = tag.upper()

    name, *attributes = tag.split()

    for item in attributes:
        if quotedstringkey is not None:
            previouskey = quotedstringkey
            # If end of quoted string
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
                # If beginning of quoted string
                if value[0] in quotes and value[-1] not in quotes:
                    quotedstringkey = key
                for quote in quotes:
                    value = value.replace(quote, "")
            tagdict[key] = value

    return name, tagdict


def tags_equal(tag1: str, tag2: str) -> bool:
    return clean_tag(tag1) == clean_tag(tag2)
