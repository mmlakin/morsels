from collections import deque

def tail(seq, n):
    if n <= 0:
        return []
    return [
        x for x in deque(seq, n)
    ]

""" Old slow way with null object:
def tail(seq,n):
    if n < 1:
        return []
    null = object()
    l = [null] * n
    for x in seq:
        l.append(x)
        l.pop(0)
    return [
        y
        for y in l
        if y != null
    ]
"""
