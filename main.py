from application import salary as s
from application.db import people as p
from datetime import datetime


def print_employees(employees):
    print('____Our friendly collective____')
    for e in employees:
        print(f"Name: {e['name']}, position: {e['position']}")


if __name__ == '__main__':
    today = datetime.today()
    print(today.date())
    print_employees(p.get_employees())
    while True:
        print(s.calculate_salary(p.get_employees(), int(input('За какое количество месяцев считаем зарплату? '))))
