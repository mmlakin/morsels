from math import pi

class Circle:
    def __init__(self, radius = 1):
        self._radius = radius

    def __repr__(self):
        return "Circle({})".format(self._radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def diameter(self):
        return (self._radius * 2)

    @diameter.setter
    def diameter(self, diameter):
        self.radius = (diameter / 2)
        self._diameter = diameter

    @property
    def area(self):
        return (pi * self._radius**2)
