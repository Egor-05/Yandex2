price = {}
itog = []

for i in range(int(input())):
    a = input().split('\t')
    price[a[0]] = int(a[1])

input()

b = 0
while 1:
    a = input()
    if a == '.':
        if b != 0:
            itog.append(b)
        break
    elif a == '':
        if b != 0:
            itog.append(b)
        b = 0
        continue
    a = a.split('\t')
    b += price[a[0]] * int(a[1])

for i in range(len(itog)):
    print(f'{i + 1}) {itog[i]}')

print(f'Итого: {sum(itog)}')
