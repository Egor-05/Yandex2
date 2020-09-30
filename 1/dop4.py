import sys


a = []
for i in sys.stdin:
    a.append(i[:-1] if '\n' in i else i)

a = ' '.join(a)
b1, c1, d1 = set(), set(), set()
e = ''
for i in a:
    if i == '.':
        b1.add(e.strip())
        e = ''
    elif i == '?':
        c1.add(e.strip())
        e = ''
    elif i == '!':
        d1.add(e.strip())
        e = ''
    if i.isalnum() or i == ' ':
        e += i.lower()
b = set()
for i in b1:
    for j in i.split():
        b.add(j)
c = set()
for i in c1:
    for j in i.split():
        c.add(j)
d = set()
for i in d1:
    for j in i.split():
        d.add(j)
f = b & c
h = f - (f & d)

print(' '.join(sorted([i for i in h])))
