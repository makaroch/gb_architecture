"""
Переписать код SpeedCalculation в соответствии с Open-Closed Principle:
class SpeedCalculation:
def calculate_allowed_speed(self, vehicle):
if vehicle.get_type().lower() == "car":
return vehicle.get_max_speed() * 0.8
elif vehicle.get_type().lower() == "bus":
return vehicle.get_max_speed() * 0.6
return 0.0

class Vehicle:
def init(self, max_speed, type):
self.max_speed = max_speed
self.type = type

def get_max_speed(self):
    return self.max_speed

def get_type(self):
    return self.type
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, max_speed: int, type: str):
        self.max_speed = max_speed
        self.type = type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type

    @abstractmethod
    def calculate_allowed_speed(self) -> float:
        pass


class Bus(Vehicle):
    def __int__(self, max_speed: int, type: str, seating: int):
        super().__init__(max_speed, type)
        self.seating = seating

    def calculate_allowed_speed(self) -> float:
        return round(self.get_max_speed() * 0.8, 2)


class Car(Vehicle):
    def __int__(self, max_speed: int, type: str, number_of_doors: int):
        super().__init__(max_speed, type)
        self.number_of_doors = number_of_doors

    def calculate_allowed_speed(self) -> float:
        return round(self.get_max_speed() * 0.6, 2)


class SpeedCalculation:
    def calculate_allowed_speed(self, vehicle: Vehicle) -> float:
        return vehicle.calculate_allowed_speed()
