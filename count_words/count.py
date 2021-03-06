#!/usr/bin/env python3
"""count.py - Take a string and return a dict of each word in the string and the number of times it appears in the string"""

from string import punctuation as punctuationmarks
import re

def count_words(line: str) -> dict:
    """ Use re.findall to return a list of words with apostrophes included """
    regex=r"[\w']+"
    linewords = re.findall(regex, line.lower())
    return {
        word:linewords.count(word)
        for word in set(linewords)
    }
