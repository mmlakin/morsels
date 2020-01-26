#!/usr/bin/env python3
"""
  float_range.py

  Create callable object like range for floats,
  with optional start and step arguments.
"""
from math import ceil

class float_range():
    """range() for floating point numbers

    Attributes:
        _start (float): starting number (incl in range)
        _end (float): ending number (not incl in range)
        _step (float): step number added in each iteration
        _num (float): current number
        _len (int): length of numbers in iterator for len()
    """

    def __init__(self, start=None, end=None, step=1.0):
        """If only one arg is given, it will be saved as end
            and start will default to 0.
        """
        if start is None:
            raise TypeError("Must supply at least one value")
        if end is None:
            end, start = start, 0.0

        # Convert all to float
        self._end, self._start, self._step = map(
            float, (end, start, step)
        )
        self._num = self._start
        self._len = int(ceil((end - start) / step))

        if self._len < 0:
            self._len = 0 # Set len to zero if range is invalid

    def __len__(self):
        return self._len

    def __iter__(self):
        while (self._end - self._num) / self._step > 0:
            num = self._num
            self._num += self._step
            yield num
        self._num = self._start

    def __reversed__(self):
        num = self._start + (self._step * (self._len-1))
        while num >= self._start:
            yield num
            num -= self._step

    def __repr__(self):
        return f"float_range({self._start}, {self._end}, {self._step})"

    def __eq__(self, other):
        try:
            if len(self) == len(other):
                if len(self) == 0:
                    return True
                same_first = next(iter(self)) == next(iter(other))
                same_last = next(reversed(self)) == next(reversed(other))
                if same_first and same_last:
                    return True
            return False
        except:
            return NotImplemented
