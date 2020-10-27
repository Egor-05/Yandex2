import csv


with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for i in reader:
        if int(i['Old price']) > int(i['New price']):
            print(i['Name'])