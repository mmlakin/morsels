#!/usr/bin/env python3
"""
month.py

A Month class to represent a specific month and year.

Month objects have two different string representations, and are comparable to each other using equality and ordering operations.  Month objects are not comparable to other types.

Bonus 1: Implement first_day and last_day attributes.

"""

import datetime
import calendar


class Month:
    """Month class Month(year, month) comparable & orderable to self"""

    def __init__(self, year, month):
        self.year, self.month = year, month

    @property
    def first_day(self):
        return datetime.date(self.year, self.month, 1)

    @property
    def last_day(self):
        _, days_in_month = calendar.monthrange(self.year, self.month)
        return datetime.date(self.year, self.month, days_in_month)

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month:02}"

    def __eq__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) == (other.year, other.month)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) < (other.year, other.month)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) > (other.year, other.month)
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) <= (other.year, other.month)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) >= (other.year, other.month)
        else:
            return NotImplemented
