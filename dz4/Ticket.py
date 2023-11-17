import decimal
import numbers
from datetime import datetime


class Ticket:
    def __init__(self, __id: numbers, __departure_zone: numbers, __arrival_zone: numbers, __route_number: numbers,
                 __departure_time: datetime, __arrival_time: datetime, __buyer_id: numbers,
                 __is_used: bool, __price: decimal, __place: str):
        self.__id: numbers = __id
        self.__departure_zone: numbers = __departure_zone
        self.__arrival_zone: numbers = __arrival_zone
        self.__route_number: numbers = __route_number
        self.__departure_time: datetime = __departure_time
        self.__arrival_time: datetime = __arrival_time
        self.__buyer_id: numbers = __buyer_id
        self.__is_used: bool = __is_used
        self.__price: decimal = __price
        self.__place: str = __place
