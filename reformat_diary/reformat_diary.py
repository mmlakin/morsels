#!/usr/bin/env python3

"""
  reformat_diary.py - Turn a text file with many diary entries into many text
  files, one for each entry
"""

import re


RE_DATE = re.compile(r"^\d{4}[-/]\d{2}[-/]\d{2}")


def clean_entry(entry):
    entry = entry.replace("&nbsp;", " ")
    entry = entry.replace("&quot;", '"')
    entry = entry.replace("&amp;", "&")
    return entry.strip()


def entries_by_date(diary_file) -> list:
    cur_date, cur_entry = None, ""
    for diary_line in diary_file:
        if RE_DATE.search(diary_line):
            if cur_date:
                yield cur_date, clean_entry(cur_entry)
            cur_date, cur_entry = diary_line.rstrip(), ""
        else:
            cur_entry += diary_line
    yield cur_date, clean_entry(cur_entry)
