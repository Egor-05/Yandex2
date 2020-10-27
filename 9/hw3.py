import csv
from collections import defaultdict


def way(p_now, arr):
    arr.append(p_now)
    for i in from_to[p_now]:
        if i == end and len(arr + [i]) <= 3:
            global ways
            arr1 = arr + [i]
            ways[sum([from_to[arr1[j]][arr1[j + 1]] for j in range(len(arr1) - 1)])] = ' '.join(arr1)
        elif i in arr:
            continue
        else:
            way(i, arr.copy())


from_to = defaultdict(dict)
ways = {}
start = 0
end = 0
with open('input.csv') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    for i in reader:
        a = i if i[-1] != '' else i[:-1]
        if len(a) == 3:
            from_to[a[0]][a[1]] = int(a[2])
        else:
            start, end = a
    way(start, [])
    print(ways[min(list(ways.keys()))])