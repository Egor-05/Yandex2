with open(input()) as f:
    a = f.read().splitlines()
with open(input()) as f:
    b = f.read().splitlines()
res = []
for i in b:
    x, y = [int(j) for j in i.split()]
    if eval(a[0]) and eval(a[1]):
        res.append((x, y))
res.sort(key=lambda x: x[1], reverse=True)
res.sort(key=lambda x: x[0])
res1 = [str(i) for i in res]
with open('relevant_points.txt', 'w') as f:
    f.write('\n'.join(res1))

