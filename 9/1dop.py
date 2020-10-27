import openpyxl
import csv


wb = openpyxl.load_workbook('data.xlsx', data_only=True)
sheet = wb.active

with open('output.csv', 'w', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"')
    for i in sheet.rows:
        value = []
        for j in i:
            j = j.value
            if type(j) == int:
                j = float(j)
            value.append(str(j) if j else '')
        writer.writerow(value)
