from random import randint


with open('lines.txt', 'r') as f:
    lst = f.read().splitlines()
if len(lst) > 0:
    print(lst[randint(0, len(lst) - 1)])
