####arg parser#######
"""
Р—Р°РїСѓРє РёР· С‚РµСЂРјРёРЅР°Р»Р° СЃ РїРѕРјРѕС‰СЊСЋ СЃР»РµРґСѓСЋС‰РµР№ СЃС‚СЂРѕРєРё:
python3 run_with_scripts.py --name Basil --age 32 --place Bar

"""
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--name', type = str)
parser.add_argument('--age', type = int)
parser.add_argument('--data_path', type = str, default = None)
parser.add_argument('--place', type = str, default='Shop')

args = parser.parse_args()
print(f"In our args {args}. Type {type(args.age)}")
print(f"Hello, {args.name}! You are {args.age}. You work in {args.place}")




# from sys import argv
#
# print(f'Our args is {argv}. It is type {type(argv)}, {type(argv[-1])}')
# script_name, name, surname = argv
# print(f'Hello, worker {name}, {surname}!')