names = dict()
for i in range(int(input())):
    a = list(input().split('@')[0])
    while a[-1].isdigit():
        del a[-1]
    a = ''.join(a)
    if a not in list(names.keys()):
        names[a] = 1
    else:
        names[a] += 1
nn = []
for i in range(int(input())):
    a = input()
    if a not in list(names.keys()):
        nn.append(a)
        names[a] = 1
    else:
        nn.append(a + str(names[a]))
        names[a] += 1
for i in nn:
    print(f'{i}@untitled.py')