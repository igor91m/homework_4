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
Не могу понять как прописать с условием for el in fact(n) по самой задаче с счетчиком.
'''
def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break

'''
Другие примеры:
#0
import math
print(math.factorial(5))

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
from math import factorial
print(f"factorial(5) -> {factorial(5)}")

#4
import math
n = int(input("Введите факториал какого числа найти: "))
res = math.factorial(n)
print(res)
'''