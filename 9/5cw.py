import csv


a = int(input())
with open('vps.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for i in reader:
        if int(i['соответствует в %']) >= a:
            print(i['Специальность'])