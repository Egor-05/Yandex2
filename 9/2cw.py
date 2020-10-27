import csv


with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    mtx = []
    for i in reader:
        mtx.append([i[0], int(i[1]), 0])
mtx.sort(key=lambda x: x[1])
money = 1000
res = []
for i in range(len(mtx)):
    while mtx[i][2] < 10:
        if money - mtx[i][1] >= 0:
            money -= mtx[i][1]
            mtx[i][2] += 1
            res.append(mtx[i][0])
        else:
            break
print(', '.join(res) if len(res) > 0 else 'error')
