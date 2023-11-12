'''
Переписать код в соответствии с Interface Segregation Principle:
from abc import ABC, abstractmethod
import math

class Shape(ABC):
@abstractmethod
def area(self):
pass

@abstractmethod
def volume(self):
    pass
class Circle(Shape):
def init(self, radius):
self.radius = radius

def area(self):
    return 2 * math.pi * self.radius

def volume(self):
    raise NotImplementedError("Circle does not have volume")
class Cube(Shape):
def init(self, edge):
self.edge = edge

def area(self):
    return 6 * self.edge * self.edge

def volume(self):
    return self.edge * self.edge * self.edge
'''

from abc import ABC, abstractmethod
import math


class FlatFigures(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class DimensionalFigures(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass


class Circle(FlatFigures):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return 2 * math.pi * self.radius


class Cube(FlatFigures, DimensionalFigures):
    def __init__(self, edge):
        self.edge = edge

    def area(self) -> float:
        return 6 * self.edge * self.edge

    def volume(self) -> float:
        return self.edge * self.edge * self.edge
