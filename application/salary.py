def calculate_salary(employees, months):
    return sum([e['salary'] * months for e in employees])
