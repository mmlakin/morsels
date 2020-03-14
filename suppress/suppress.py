#!/usr/env/python3
"""
 suppress.py
 A context manager that will suppress given error types.
 e.g.
      >>> with suppress(NameError):
      ...     print("Hi!")
      ...     print("Nice to meet you, ", name)
      Hi!
"""


class suppress:
    def __init__(self, *errortypes):
        self.errortypes = errortypes
        self.exception, self.traceback = None, None

    def __enter__(self):
        return self

    def __exit__(self, err_type, err_val, traceback):
        if isinstance(err_val, self.errortypes):
            self.exception = err_val
            self.traceback = traceback
            return True
