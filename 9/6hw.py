import csv
import sys


n, m = [int(i) for i in input().split()]

results = []
for i in sys.stdin:
    results.append(i.strip().split())

with open('exam.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Фамилия', 'имя', 'результат 1', 'результат 2',
                     'результат 3', 'сумма'])
    for i in results:
        lst = [int(j) for j in i[2:]]
        if sum(lst) >= n and min(lst) >= m:
            writer.writerow(i + [str(sum(lst))])