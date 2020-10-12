with open('plant.txt', 'r', encoding='utf-8') as f:
    a = f.read()
b = a.lower()
res = []
for i in range(len(a)):
    if b.count(b[i]) == 2:
        res.append(a[i])
with open('double.txt', 'w') as f:
    f.write(''.join(res))