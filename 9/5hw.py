import csv


with open('salary.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    name = input()
    years = input().split()
    objects = [['Субъект', years[0], years[1]]]
    for i in reader:
        if i['Федеральный округ'] == name:
            if int(i[years[0]]) + int(i[years[0]]) / 25 > int(i[years[1]]):
                objects.append([i['Субъект'], i[years[0]], i[years[1]]])

with open('out_file.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    if len(objects) > 1:
        writer.writerows(objects)
