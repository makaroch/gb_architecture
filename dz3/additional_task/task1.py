"""
1) Переписать код в соответствии с Single Responsibility Principle:
from datetime import date
class Employee:
def init(self, name, dob, base_salary):
self.name = name
self.dob = dob
self.base_salary = base_salary

def get_emp_info(self):
    return f"name - {self.name} , dob - {self.dob}"

def calculate_net_salary(self):
    tax = int(self.base_salary * 0.25)  # рассчитать налог другим способом
    return self.base_salary - tax
"""


class Employee:
    def __init__(self, name: str, dob: int, base_salary: int):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"


class Accounting:
    def __int__(self):
        pass

    def calculate_net_salary(self, employee: Employee) -> int:
        if employee.base_salary is None:
            raise TypeError("base_salary is none")
        tax = int(employee.base_salary * 0.25)  # рассчитать налог другим способом
        return employee.base_salary - tax
