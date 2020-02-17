#!/usr/bin/env python3
"""
month.py

A Month class to represent a specific month and year.

Month objects have two different string representations, and are comparable to each other using equality and ordering operations.  Month objects are not comparable to other types.

Bonus 1: Implement first_day and last_day attributes.
Bonus 2: Implement from_date() factory function and strftime() instance method.
Bonus 3: Make Month objects memory efficient, immutable, and hashable

"""

import datetime
import calendar
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Month:
    """Month class Month(year, month) comparable & orderable to self"""

    year: int
    month: int

    __slots__ = ["year", "month"]

    def from_date(from_date_object):
        return Month(from_date_object.year, from_date_object.month)

    def strftime(self, strftime_format_string):
        return self.first_day.strftime(strftime_format_string)

    @property
    def first_day(self):
        return datetime.date(self.year, self.month, 1)

    @property
    def last_day(self):
        _, days_in_month = calendar.monthrange(self.year, self.month)
        return datetime.date(self.year, self.month, days_in_month)

    def __str__(self):
        return f"{self.year}-{self.month:02}"
