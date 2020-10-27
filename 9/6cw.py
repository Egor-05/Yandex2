import csv
import sys


rows = [['nomen', 'definitio', 'pluma', 'Russian nomen', 'familia', 'Russian nomen familia']]
for i in sys.stdin:
    rows.append(i.strip().split('\t'))

with open('plantis.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerows(rows)
