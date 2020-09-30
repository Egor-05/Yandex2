a = input().replace(' ', '')
ok = True

if a[0] != '8' and a[:2] != '+7':
    ok = False
elif a.count('(') != a.count(')') or a.count('(') > 1:
    ok = False
elif a[0] == '-' or a[-1] == '-':
    ok = False
else:
    for i in range(1, len(a)):
        if a[i] == a[i - 1] == '-':
            ok = False
if ok:
    res = '+'
    if a[0] == '8':
        a = '7' + a[1:]
    for i in a:
        if i.isdigit():
            res += i
    print(res if len(res) == 12 else 'error')
else:
    print('error')

