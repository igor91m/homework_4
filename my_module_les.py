def my_div(num_1, num_2):
    try:
        res = num_1 / num_2
    except ZeroDivisionError:
        print("Что-то идет не так")
        res = 0
    return res

def my_div_str(num_1, num_2):
    try:
        res = float(num_1) / float(num_2)
    except ZeroDivisionError:
        print("Что-то идет не так")
        res = 0
    return res

