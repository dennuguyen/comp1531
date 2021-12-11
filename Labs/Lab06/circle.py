"""
circle.py
"""

from math import pi


class Circle():
    """
    Circle with single attribute radius and two methods circumference and area.
    """
    def __init__(self, radius):
        """
        Constructor accepts a radius.
        """
        self._radius = float(radius)

    @property
    def radius(self):
        """
        Return the radius
        """
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        """
        Set a new radius.
        """
        self._radius = new_radius

    @radius.deleter
    def radius(self):
        """
        Delete radius cause why not.
        """
        del self._radius

    @property
    def circumference(self):
        """
        Returns circumference of circle to 1 decimal place.
        """
        return round(2 * pi * self._radius, 1)

    @property
    def area(self):
        """
        Returns area of circle to 1 decimal place.
        """
        return round(pi * self._radius**2, 1)


if __name__ == "__main__":
    circle = Circle(input("Please enter a radius: "))
    print(f"Circumference: {circle.circumference}")
    print(f"Area: {circle.area}")
