#!/usr/bin/env python3
"""
month.py

This week I'd like you to create a Month class which represents a specific month in a specific year.

>>> dec99 = Month(1999, 12)
>>> dec99
Month(1999, 12)
>>> print(dec99)
1999-12

Month objects should have two different string representations (see above). They should also be comparable to each other using equality and ordering operators:

>>> sorted([Month(1998, 12), Month(2000, 1), Month(1999, 12)])
[Month(1998, 12), Month(1999, 12), Month(2000, 1)]

Month objects should not be comparable to tuples, lists, date objects, or other non-Month objects (just as tuples and lists are not comparable to each other).

>>> Month(1998, 12) < (1998, 12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Month' and 'tuple'
"""


class Month:
    def __init__(self, year, month):
        self.year, self.month = year, month

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
