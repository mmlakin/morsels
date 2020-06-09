#!/usr/bin/env python3

"""
 tags_equal.py

 Take two strings containing opening HTML tags and return True if they have
 the same attributes with the same values.
"""


import shlex


def clean_tag(tag: str) -> tuple:
    """Return a tuple containing the tag name and a dict of the tag's
        attributes, respecting the first value set for an attribute"""
    tagdict = dict()

    # Remove brackets around tag
    tag = tag[1:-1]

    tag = tag.upper()

    name, *attributes = shlex.split(tag)

    for item in attributes:
        item = item.split("=")
        key = item[0]
        value = item[1] if len(item) > 1 else ""
        tagdict.setdefault(key, value)

    return name, tagdict


def tags_equal(tag1: str, tag2: str) -> bool:
    """Return true if the tags contain equal values"""
    return clean_tag(tag1) == clean_tag(tag2)
