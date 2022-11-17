import math
from behavior_sim.geometry.geom2d import Point2D, Line2D
from behavior_sim import utilities

def test_line2d_len():

    a = Point2D(0, 0)
    b = Point2D(0, 3)

    l = Line2D(a, b)

    assert l.length == 3

    c = Point2D(3, 3)

    l2 = Line2D(a, c)

    assert l2.length == utilities.dec_round(math.sqrt(18))

def test_pdist():

    a = Point2D(0, 0)
    b = Point2D(0, 3)
    c = Point2D(3, 3)

    l = Line2D(a, b)

    assert l.p_dist(c) == utilities.dec_round(3)

    d = Point2D(0, 5)
    e = Point2D(-2.5, 0)
    
    l2 = Line2D(d, e)

    assert l2.p_dist(c) == utilities.dec_round(8*math.sqrt(5)/5)