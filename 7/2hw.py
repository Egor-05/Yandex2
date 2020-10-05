from math import sqrt


a = ['b', 'Kb', 'Mb', 'Gb']
with open('input.txt', 'r') as f:
    lst = f.read().splitlines()
lst = [i.split() for i in lst]
b = {}
for i in lst:
    if i[0].split('.')[1] not in list(b.keys()):
        b[i[0].split('.')[1]] = [[i[0], int(i[1]), i[2]]]
    else:
        b[i[0].split('.')[1]].append([i[0], int(i[1]), i[2]])
for i in b:
    b[i].sort(key=lambda x: x[0])
for i in b:
    c = 0
    for j in b[i]:
        if a.index(j[2]) > c:
            c = a.index(j[2])
    for j in range(len(b[i])):
        b[i][j][1] /= 1024 ** (c - a.index(b[i][j][2]))
        b[i][j][2] = a[c]
with open('output.txt', 'w') as f:
    for i in sorted(list(b.keys())):
        for j in b[i]:
            f.write(j[0] + '\n')
        f.write('----------\n')
        s = 0
        for j in b[i]:
            s += j[1]
        if a.index(b[i][0][2]) < 3 and s // 1024 > 0:
            s1 = s
            while s / 1024 > 1:
                s /= 1024
                b[i][0][2] = a[a.index(b[i][0][2]) + 1]
        f.write(f'Summary: {round(s)} {b[i][0][2]}\n\n')
