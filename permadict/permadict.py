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


class PermaDict(dict):
    def __setitem__(self, key, value):
        print(f"key: {key} - value: {value}")
        key = str(key)
        if key in self.keys():
            raise KeyError("Unable to set values in PermaDict.")
        else:
            setattr(self, key, value)

    def __eq__(self, other):
        return self.items() == other
