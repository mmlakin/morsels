#!/usr/bin/env python3

"""
 PermaDict.py

 A dictionary-like class that disallows keys to be updated (only added
 or removed).

 It also has keys, values, and items methods and is iterable just like
 a dict.

 Unlike a dict, when a value is set for a key that already exists, a
 KeyError exception is raised

"""


class PermaDict:
    VERBOSE = False

    def __init__(self, init=None, *, silent=False, **kwargs):
        if self.VERBOSE:
            print(f"init_kwargs:{kwargs}")
        self._dict = dict()
        self._silent = silent
        if init is not None:
            self.update(init)
        if kwargs is not None:
            self.update(kwargs)

    def __setitem__(self, key, value):
        if key in self.keys():
            if self._silent is False:
                raise KeyError("Unable to set values in PermaDict.")
            return
        if self.VERBOSE is True:
            print(f"Setting {key} to {value}")
        self._dict[key] = value

    def __delitem__(self, item):
        del self._dict[item]

    def __getitem__(self, item):
        return self._dict[item]

    def __eq__(self, other):
        return self._dict == other

    def __repr__(self):
        return str(self._dict)

    def __iter__(self):
        yield from self._dict.keys()

    def keys(self):
        return self._dict.keys()

    def values(self):
        return self._dict.values()

    def items(self):
        return self._dict.items()

    def pop(self, key):
        return self._dict.pop(key)

    def force_set(self, key, value):
        self._dict[key] = value

    def update(self, update_iter=None, *update_dicts, force=False, **update_kwargs):
        if self.VERBOSE:
            print(f"update_iter: {update_iter}")
            print(f"update_dicts: {update_dicts}")
        if update_iter:
            try:
                for k, v in update_iter:
                    if force is True:
                        self.force_set(k, v)
                    else:
                        self[k] = v
            except (ValueError, TypeError):
                for k in update_iter:
                    if force is True:
                        self.force_set(k, update_iter[k])
                    else:
                        self[k] = update_iter[k]
        if update_dicts:
            for update_dict in update_dicts:
                if force is True:
                    self.force_set(k, update_dict[k])
                else:
                    self[k] = update_dict[k]

        if update_kwargs:
            for k in update_kwargs:
                if force is True:
                    self.force_set(k, update_kwargs[k])
                else:
                    self[k] = update_kwargs[k]
