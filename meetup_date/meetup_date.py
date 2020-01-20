#!/usr/bin/env python3
"""
meetup_date.py

Given a year and month, find date of certain recurring meetings

"""
from datetime import (date, timedelta)
ONE_DAY=timedelta(days=1)

def meetup_date(year, month, nth=4, weekday=3):
    """takes year and month and returns
    datetime object"""
    nth-=1
    dt = date(year, month, 1)
    while True:
        if dt.weekday() == weekday:
            break
        dt += ONE_DAY
    dt += timedelta(days=nth*7)
    return dt
