ENG = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
RUS = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']


def prov(word):
    for i in ENG:
        if word in i:
            return False
    for i in RUS:
        if word in i:
            return False
    return True


a = input()
ok = False
if len(a) > 8:
    dig = False
    big = False
    small = False
    for i in a:
        if not dig and i.isdigit():
            dig = True
        if not big and i.isupper():
            big = True
        if not small and i.islower():
            small = True
    if dig and big and small:
        ok = True
        a = a.lower()
        for i in range(len(a) - 2):
            ok = prov(a[i: i + 3])
print('ok' if ok else 'error')