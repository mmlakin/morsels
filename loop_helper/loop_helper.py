from itertools import tee


class LoopInfo:
    def __init__(self, previous_default, next_default):
        self.is_first = True
        self.is_last = False
        self.index = 0
        self.current = None
        self.previous = previous_default


def loop_helper(iterable, previous_default=None, next_default=None):
    info = LoopInfo(previous_default, next_default)
    cur_iter, next_iter = tee(iterable, 2)
    while True:
        try:
            info.current = next(cur_iter)
            if info.is_first is True:
                next(next_iter)
        except StopIteration:
            break
        try:
            info.next = next(next_iter)
        except StopIteration:
            info.next = next_default
            info.is_last = True
        yield (info.current, info)
        if info.is_last is True:
            break
        info.previous = info.current
        if info.is_first is True:
            info.is_first = False
        info.index += 1
