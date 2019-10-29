#!/usr/bin/env python3

"""
count.py - Take a string and return a dict of each word in the string and the number of times it appears in the string.
"""

from string import punctuation as punctuationmarks

def count_words(line: str) -> dict:
    """

    """

    linewords = line.lower().split(' ')

    return {
        word.strip(punctuationmarks):linewords.count(word)
        for word in set(linewords)
    }
