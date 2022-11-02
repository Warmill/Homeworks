from decimal import Decimal
from datetime import date

from classes import Employee
from decorator import timer

employees = [
    Employee(name="John", start=date(2022, 5, 20), rate=Decimal("11"), taxes=10),
    Employee(name="Alex", start=date(2022, 5, 1), rate=Decimal("50"), taxes=20),
    Employee(name="Kseniya", start=date(2022, 5, 10), rate=Decimal("50"), taxes=40),
    Employee(name="Valeriy", start=date(2022, 4, 20), rate=Decimal("60"), taxes=50),
    Employee(name="Vera", start=date(2019, 5, 20), rate=Decimal("99"), taxes=60),
    Employee(name="Suzanna", start=date(2021, 5, 20), rate=Decimal("20"), taxes=10),
    Employee(name="Gleb", start=date(2021, 5, 20), rate=Decimal("20"), taxes=10),
]
johh= Employee(name="John", start=date(2022, 5, 20), rate=Decimal("11"), taxes=10)

@timer(func_name="Show table")
def show_table():
    Employee.show_header()
    for emp in employees:
        Employee.show_row(emp)
        Employee.show_line()


def update_table():
    for emp in employees:
        Employee.update_rate(emp,emp.rate)


if __name__ == "__main__":
    show_table()
    update_table()
    show_table()