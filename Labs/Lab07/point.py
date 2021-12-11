"""
Point Class
"""
from math import sqrt, atan2, cos, sin, isclose, pi


class Point:
    """
    Point class stores x, y but has radius and theta methods
    """
    def __init__(self, x, y):
        """
        Constructor
        """
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        """
        x
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        x setter
        """
        self._x = x

    @property
    def y(self):
        """
        y
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        y setter
        """
        self._y = y

    @property
    def theta(self):
        """
        theta
        """
        return atan2(self._y, self._x)

    @theta.setter
    def theta(self, theta):
        """
        theta setter
        """
        temp_r = self.r
        self._x = temp_r * cos(theta)
        self._y = temp_r * sin(theta)

    @property
    def r(self):
        """
        r
        """
        return sqrt(self._x**2 + self._y**2)

    @r.setter
    def r(self, r):
        """
        r setter
        """
        temp_theta = self.theta
        self._x = r * cos(temp_theta)
        self._y = r * sin(temp_theta)


def distance(start, end):
    """
    Calculate the distance between 2 points.
    """
    return sqrt((end.x - start.x)**2 + (end.y - start.y**2))


def test_point():
    """
    test_point
    """
    me = Point(1, 1)
    my_house = Point(2, 1)
    assert isclose(distance(me, my_house), 1,
                   rel_tol=0.01)  # Within 1% tolerance
    me.x = 2
    assert isclose(distance(me, my_house), 0, rel_tol=0.01)
    me.y = 0
    assert isclose(me.r, 2, rel_tol=0.01)
    assert isclose(me.theta, 0, rel_tol=0.01)
    me.r = 3
    assert isclose(me.x, 3, rel_tol=0.01)
    me.theta = pi * 0.25  # 45 degrees in radians
    assert isclose(me.x, 3 * cos(pi * 0.25), rel_tol=0.01)
    assert isclose(me.y, 3 * cos(pi * 0.25), rel_tol=0.01)
