ENG = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
RUS = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']


def check_letters(letters, lang):
    for j in lang:
        if letters in j:
            errors[3] += 1


def check_password(password):
    if len(password) <= 8:
        errors[1] += 1
    if password.isupper() or password.islower() or password.isdigit():
        errors[2] += 1
    dig = False
    for i in password:
        if not dig and i.isdigit():
            dig = True
    if not dig:
        errors[0] += 1
    password = password.lower()
    for i in words:
        if i in password:
            errors[4] += 1
    for i in range(len(password) - 2):
        word = password[i:i + 3]
        check_letters(word, ENG)
        check_letters(word, RUS)
    return 'ok'


with open('top 10000 passwd.txt', 'r') as f:
    lst = f.read().splitlines()
with open('top-9999-words.txt', 'r') as f1:
    words = f1.read().splitlines()
errors = [0, 0, 0, 0, 0]
types_errors = ['DigitError',
                'LengthError',
                'LetterError',
                'SequenceError',
                'WordError']
for i in lst:
    check_password(i)
for i in range(5):
    print(f'{types_errors[i]} - {errors[i]}')

