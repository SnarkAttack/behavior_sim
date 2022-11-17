from abc import ABC, abstractmethod
import math
from .. import utilities

class Entity(ABC):

    def __init__(self):
        pass

class TypedEntity(Entity):

    def __init__(self, type_id):
        self.type_id = type_id

class Movable2DEntity(Entity):

    def __init__(self, speed=0, dir=0, start_x=0, start_y=0):
        self.speed = speed
        # Saved in radians
        self.dir = dir

        self.x = start_x
        self.y = start_y

    def move(self):
        self.x += utilities.dec_round(self.speed*math.cos(self.dir))
        self.y += utilities.dec_round(self.speed*math.sin(self.dir))

class TypedMovableEntity(TypedEntity, Movable2DEntity):
    
    def __init__(self, type_id, speed=0, dir=0, start_x=0, start_y=0):
        super(TypedEntity, self).__init__(type_id)
        super(Movable2DEntity, self).__init__(speed, dir, start_x, start_y)