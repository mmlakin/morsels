#!/usr/bin/env python3


def window(input_numbers, window_size):
    seen = []
    for x in input_numbers:
        seen.append(x)
        if len(seen) >= window_size:
            yield tuple(seen[-window_size:])
