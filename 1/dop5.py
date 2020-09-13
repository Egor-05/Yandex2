import sys


sub = {}
for i in sys.stdin:
    a = i.split()
    if len(a) > 1:
        a = [' '.join(a[:-1]), a[-1]]
        if int(a[1]) not in list(sub.keys()):
            sub[int(a[1])] = []
        if a[0] not in sub[int(a[1])]:
            sub[int(a[1])].append(a[0])
for i in sorted(list(sub.keys())):
    print(f'{i}: {", ".join(sub[i])}')