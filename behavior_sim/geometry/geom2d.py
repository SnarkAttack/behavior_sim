import math
from .. import utilities

class Point2D():

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    @classmethod
    def dist(a, b):
        return Line2D(a, b).length


class Line2D():

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a
    
    @property
    def b(self):
        return self._b

    @property
    def length(self):
        dx = self.a.x-self.b.x
        dy = self.a.y-self.b.y
        return utilities.dec_round(math.sqrt(dx**2 + dy**2))

    def p_dist(self, p):
        return utilities.dec_round(abs((self.b.x-self.a.x)*(self.a.y-p.y)- \
                                    (self.a.x-p.x)*(self.b.y-self.a.y)) / \
                                    math.sqrt((self.a.x-self.b.x)**2+(self.a.y-self.b.y)**2))