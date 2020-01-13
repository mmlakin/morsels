#!/usr/bin/env python3
"""
  deep_add.py - Add lists and lists of lists and anything
"""

from collections.abc import Iterable

def deep_add(item, start=0):
    """ Adds up values in nested iterables """
    zero=start-start    # value 0 of type(start)
    return (
        item if not isinstance(item,Iterable)
        else sum((
            deep_add(i, zero)
            for i in item
        ), start)    # sum() start variable
    )

# def deep_add(item, start=0):
#     zero=start-start # value 0 of type(start)
#     if not isinstance(item, Iterable):
#         return item
#     else:
#         return sum(
#             (deep_add(i, zero)
#              for i in item
#             ), start)

# def deep_add(item, start=0):
#     if isinstance(item, Iterable):
#         total = start
#         for i in item:
#             total = deep_add(i, start=total)
#         return total
#     else:
#         return item + start

# def deep_add(item, start=0):
#     total = start
#
#     lists = list(item)
#     while lists:
#         i = lists.pop()
#         if isinstance(i, Iterable):
#             lists.extend(i)
#         else:
#             total += i
#     return total
#
# def deep_add(item, start=0):
#     if isinstance(item, Iterable):
#         total = start
#         for i in item:
#             total = deep_add(i, start=total)
#         return total
#     else:
#         return item + start

# def deep_add(item, start=0):
#     if isinstance(item, Iterable):
#         return sum((deep_add(i, start=start-start) for i in item), start)
#     else:
#         return item

# def deep_add(item, start=0):
#     if not isinstance(item, Iterable):
#         return item
#     else:
#         return sum((deep_add(i,start=start-start) for i in item), start)
