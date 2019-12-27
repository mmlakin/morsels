#!/usr/bin/env python3

"""
EasyDict creates objects that can use key lookups and attribute lookups interchangeably.

    EasyDict accepts a dictionary and/or keyword arguments to define the object's attributes

    e.g. >>> bob = EasyDict({'name':'Bob', 'age':57})
        >>> bob['name']
        'Bob'
        >>> bob.age
        57

    EasyDict takes a 'normalize' keyword to convert spaces in keys to underscores for attribute names:

    e.g. >>> jim = EasyDict({'name':'Jim', normalize=True, })

"""

class EasyDict():
    """ EasyDict object uses key & attribute lookups """

    def __init__(self, mapping = {}, *, normalize = False, **kwargs):
        startdict = {}
        try:
            startdict.update(mapping)
            startdict.update(kwargs)
        except:
            raise self.UnableToUpdateDictWithInput(mapping)

        self._normalize = normalize

        for key,value in startdict.items():
            setattr(self, self.normalized(key), value)

    def normalized(self, key):
        return key.replace(' ', '_') if self._normalize else key

    def get(self, key, default = None):
        try:
            return getattr(self, self.normalized(key))
        except:
            return default

    def __getitem__(self, key):
        return getattr(self, self.normalized(key))

    def __setitem__(self, key, value):
        setattr(self, self.normalized(key), value)

    def __eq__(self, other):
        try:
            return self.__dict__ == other.__dict__
        except:
            return False

    def __repr__(self):
        return f"{self.__dict__}"

    class UnableToUpdateDictWithInput(ValueError):
        pass

