import numbers
from typing import List

from dz4 import Ticket


class User:
    def __init__(self, id: numbers, name: str, tickets: List[Ticket],
                 login: str, passwd_hash: numbers, account_id: numbers):
        self.__id: numbers = id
        self.__name: str = name
        self.__tickets: List[Ticket] = tickets
        self.__login: str = login
        self.__passwd_hash: numbers = passwd_hash
        self.__account_id: numbers = account_id
