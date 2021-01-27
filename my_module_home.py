def salary():
    try:
        output_in_hours = float(input("Выроботка в часах: "))
        rate = float(input("Ставка в час: "))
        bonus = float(input("Премия: "))
        tax_13 = 0.13
        sum_tax = ((output_in_hours * rate) + bonus) * tax_13
        salary_without_tax = (output_in_hours * rate) + bonus
        total_salary = salary_without_tax - sum_tax
        print(f"Заработная плата сотрудника до вычета налога: {round(salary_without_tax, 2)} рублей")
        print(f"Налог составил: {round(sum_tax, 2)} рублей")
        print(f"Заработная плата сотрудника после вычета налога: {round(total_salary, 2)} рублей")
    except ZeroDivisionError:
        return print("Не те числа")