from math import sqrt


a = int(input())
b = sqrt(a)
if int(b) == b:
    if a % 2 == 0:
        print(int(b), 1)
    else:
        print(1, b)
else:
    c = (int(b) + 1) ** 2
    if c - (c - (int(b) ** 2 + 1)):
        print(c, c)
    elif c % 2 == 0:
        print(c, 1 + c - a)
    else:
        print(1 + c - a, c)