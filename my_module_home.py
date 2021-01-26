def salary():
    try:
        output_in_hours = float(input("Выроботка в часах: "))
        rate = float(input("Ставка в час: "))
        bonus = float(input("Премия: "))
        tax_13 = 0.13
        sum_nalog = ((output_in_hours * rate) + bonus) * tax_13
        sum_without_nalog = (output_in_hours * rate) + bonus
        total_sum = sum_without_nalog - sum_nalog
        print(f"Заработная плата сотрудника до вычета налога: {round(sum_without_nalog, 2)}")
        print(f"Заработная плата сотрудника после вычета налога: {round(total_sum, 2)}")
    except ZeroDivisionError:
        return print("Не те числа")