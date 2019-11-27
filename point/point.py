"""
The Point class must accept 3 values on initialization (x, y, and z) and have x, y, and z attributes. It must also have a helpful string representation. Additionally, point objects should be comparable to each other (two points are equal if their coordinates are the same and not equal otherwise).

"""

class Point:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return "Point(x={}, y={}, z={})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        try:
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)
        except:
            return False

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, mul):
        return Point(self.x * mul, self.y * mul, self.z * mul)

    def __rmul__(self, mul):
        return Point(self.x * mul, self.y * mul, self.z * mul)

    def __iter__(self):
        yield from (self.x, self.y, self.z)
