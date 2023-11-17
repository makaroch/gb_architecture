import decimal
import numbers


class Account:
    def __init__(self, user_account_id: numbers, balance: decimal):
        self.__user_account_id: numbers = user_account_id
        self.__balance: decimal = balance
