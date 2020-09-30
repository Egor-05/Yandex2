def form():
    if a[0] != '+' and a[0] != '8':
        raise Exception
    if a[:2] == '+1' or a[:3] == '+55' or a[:4] == '+359':
        global ac
        ac = True


def len_check():
    if len(str(a)) != 11:
        raise Exception


def first_num_check():
    if a[0] != '8' and a[:2] != '+7' and a[:2] != '+1' and a[:3] != '+55' and a[:4] != '+359':
        raise Exception


def check():
    if a.count('(') != a.count(')') or a.count('(') > 1:
        raise Exception


def check2():
    for i in range(1, len(a)):
        if a[i] == a[i - 1] == '-':
            raise Exception


def check_operator(a):
    if int(str(a)[1:4]) not in operators:
        raise Exception


a = input()
res = '+'
ok = True
operators = [910, 911, 912, 913, 914, 915, 916, 917, 918, 919,
             980, 981, 982, 983, 984, 985, 986, 987, 988, 989,
             920, 921, 922, 923, 924, 925, 926, 927, 928, 929,
             930, 931, 932, 933, 934, 935, 936, 937, 938, 939,
             902, 903, 904, 905, 906,
             960, 961, 962, 963, 964, 965, 966, 967, 968, 969]
a = a.replace(' ', '')
a = a.replace('\t', '')
ac = False
try:
    form()
except Exception:
    print('неверный формат')
    ok = False

if ok:
    try:
        first_num_check()
    except Exception:
        print('не определяется код страны')
        ok = False

if ok:
    try:
        check2()
    except Exception:
        print('неверный формат')
        ok = False

if ok:
    try:
        check()
    except Exception:
        print('неверный формат')
        ok = False

if a[0] == '+':
    a = a[1:]
a = a.replace('(', '')
a = a.replace(')', '')
a = a.replace('-', '')

if ok:
    try:
        a = int(a)
    except Exception:
        print('неверный формат')
        ok = False

if ok:
    try:
        len_check()
    except Exception:
        print('неверное количество цифр')
        ok = False
if ok and not ac:
    try:
        check_operator(a)
    except Exception:
        print('не определяется оператор сотовой связи')
        ok = False
if ok:
    if a >= 80000000000:
        a -= 10000000000
    print(res + str(a))
