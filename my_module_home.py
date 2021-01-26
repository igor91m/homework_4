def salary():
    try:
        output_in_hours = int(input("Выроботка в часах: "))
        rate = int(input("Ставка в час: "))
        bonus = int(input("Премия: "))
        result = (output_in_hours * rate) + bonus
        print(f"Заработная плата сотрудника до вычета налога: {result}")
    except ZeroDivisionError:
        return print("Не те числа")