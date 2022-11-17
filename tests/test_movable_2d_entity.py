from behavior_sim.entities.entity import Movable2DEntity
from behavior_sim import utilities

import math

def test_2d_movement():

    e = Movable2DEntity(speed=1, dir=0)
    e.move()

    assert e.x == 1
    assert e.y == 0

    e2 = Movable2DEntity(speed=1, dir=math.pi/2)
    e2.move()

    assert e2.x == 0
    assert e2.y == 1

    e3 = Movable2DEntity(speed=1, dir=math.pi/4)
    e3.move()

    assert e3.x == utilities.dec_round(math.sqrt(.5), 3)
    assert e3.y == utilities.dec_round(math.sqrt(.5), 3)