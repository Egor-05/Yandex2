import csv


with open('rez.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    number, klass = [i.rjust(2, '0') for i in input().split()]
    students = []
    for i in reader:
        if i['login'].split('-')[2] == number and \
           i['login'].split('-')[3] == klass:
            students.append([i['user_name'].split()[3], i['Score']])
    students.sort(key=lambda x: x[0], reverse=True)
    students.sort(key=lambda x: int(x[1]), reverse=True)
    for i in students:
        print(' '.join(i))


