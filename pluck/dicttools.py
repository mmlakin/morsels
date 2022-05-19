#!/usr/bin/env python3

NULL_OBJ = object()  # Used to preserve None as a default


def pluck(data:dict, *paths:tuple, sep='.', default=NULL_OBJ):
    """ Pluck items from a dictionary using delimited path strings. """

    def _pluck_one(path):
        """ Parse delimited path string and return item. """
        item = data
        for key in path.split(sep):
            try:
                item = item[key]
            except KeyError:
                if default is not NULL_OBJ:
                    return default
                else:
                    raise
        return item

    if len(paths) == 1:
        paths = paths[0]
        return _pluck_one(paths)
    else:
        return tuple(_pluck_one(path) for path in paths)
