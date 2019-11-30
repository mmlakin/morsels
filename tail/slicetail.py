def tail(iterable, n):
    """Return the last n items of given iterable."""
    sequence = list(iterable)
    if n <= 0:
        return []
    return sequence[-n:]
