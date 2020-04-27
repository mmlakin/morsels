#!/usr/bin/env python3

"""
 interleave2.py

Accepts two iterables and returns a new iterable with each of the
 items interleaved.

"""
from itertools import zip_longest


def interleave(*passed_iters) -> iter:
    nullobj = object()
    for items in zip_longest(*passed_iters, fillvalue=nullobj):
        for item in items:
            if item is not nullobj:
                yield item
