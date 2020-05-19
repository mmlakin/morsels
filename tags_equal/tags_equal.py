#!/usr/bin/env python3

"""
 tags_equal.py

 Take two strings containing opening HTML tags and return True if they have
 the same attributes with the same values.
"""


def clean_tag(tag: str) -> list:
    tag = tag.replace("<", "")
    tag = tag.replace(">", "")
    tag = tag.replace("'", "")
    tag = tag.replace('"', "")

    tag = tag.upper()
    tag = tag.split(" ")
    return set(tag)


def tags_equal(tag1: str, tag2: str) -> bool:
    return clean_tag(tag1) == clean_tag(tag2)
