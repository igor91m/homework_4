'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''
from itertools import count
from math import factorial
'''
Не могу понять как прописать с условием for el in fact(n) по самой задаче с счетчиком
'''

import math
print(math.factorial(5))

'''
Другие примеры:

#1
n = int(input("Введите факториал какого числа найти: "))
fact = 1
while n > 1:
    fact *= n
    n -= 1
print(fact)

#2
from math import factorial
print(f"Факториал числа: {factorial(int(input()))}")

#3
import math
n = int(input("Введите факториал какого числа найти: "))
res = math.factorial(n)
print(res)
'''