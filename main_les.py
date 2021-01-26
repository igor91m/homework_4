# import my_module
import numpy as np
# import my_module as md
from my_module import my_div, my_div_str

x = my_div(6, 2)
x = my_div_str('8', '2')
# print(type(np.array([1,2,3])))

#### import and import from time, random, os #######
import time
import os
import random

# for i in range(5):
#     print(f"Hello. It is {i}")
#     time.sleep(10)

files = os.listdir('/home/kompaso/AIDA/rcognita_2021/data/2021-01-18/13h/mode_1')
# path = os.getcwd()
# # os.mkdir('test_folder')
# os.rmdir('test_folder')
# print(path)
# print(files)

# range_test = list(range(1,30,5))
# random_list = random.randrange(1, 30, 5)
# print(range_test, random_list)
#
# ids = [12, 17, 16, 90, 100]
#
# print(random.sample(ids, 2))
#
# random.shuffle(ids)
# print(ids)

### РіРµРЅРµСЂР°С‚РѕСЂС‹ #####
#Task: РЅР°РїРёСЃР°С‚СЊ СЃРІРѕР№ РіРµРЅРµСЂР°С‚РѕСЂ РґР»СЏ СЃС‡РёС‚С‹РІР°РЅРёСЏ С„Р°Р№Р»РѕРІ РѕРґРёРЅ СЂР°Р·
random_str = ['cat', 'dog', '3', 'mouse', '1']
new_random_list = []
for el in random_str:
    new_random_list.append(el.title())
# print(new_random_list)

better_new_random_str = (el.title() if el.isdigit() == False else el for el in random_str)
print([el for el in better_new_random_str])
# print([el for el in better_new_random_str])
# print(better_new_random_str)


### yield ####

def my_gen(num):
    for el in range(num):
        el += 10
        yield el

x = my_gen(6)
y = my_gen(6)
print([el for el in x])
print([el for el in y])


### functools Рё itertools ###
from functools import reduce
# Task РїРѕРїСЂРѕР±РѕРІР°С‚СЊ Р·Р°РјРµРЅРёС‚СЊ РЅР° Р»СЏРјР±РґР° С„СѓРЅРєС†РёСЋ my_f
# Task РїРѕРїСЂРѕР±РѕРІР°С‚СЊ СЃРґРµР»Р°С‚СЊ СЂРµРєСѓСЂСЃРёРІРЅС‹Р№ РІС‹Р·РѕРІ

def my_f(symbol_1, symbol_2):
    return symbol_1 + symbol_2

random_str = ['a', 'b', 'c', 'b', 'd']
print(reduce(my_f, random_str))

### math ###
import math
print(math.sqrt(math.pi))

###itertools ###
from itertools import count, cycle

# for el in count(10, 20):
#     print(el)
#     time.sleep(1)
#     if el > 50:
#         break

random_str = ['a', 'b', 'c', 'b', 'd'] # first in first out FIFO
iter_str = cycle(random_str)

for i in range(10):
    print(next(iter_str))
# print(next(iter_str))
# print(next(iter_str))
# print(next(iter_str))
# print(next(iter_str))
# print(next(iter_str))
# print(next(iter_str))
# print(next(iter_str))
# print(next(iter_str))