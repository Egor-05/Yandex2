ENG = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
RUS = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']


def check_letters(letters, lang):
    for j in lang:
        if letters in j:
            raise SequenceError


def check_password(password):
    if len(password) <= 8:
        raise LengthError
    if password.isupper() or password.islower() or password.isdigit():
        raise LetterError
    dig = False
    for i in password:
        if not dig and i.isdigit():
            dig = True
    if not dig:
        raise DigitError
    password = password.lower()
    for i in range(len(password) - 2):
        word = password[i:i + 3]
        check_letters(word, ENG)
        check_letters(word, RUS)
    return 'ok'


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


c = True
while c:
    try:
        b = input()
        a = check_password(b)
        if a == 'ok':
            print('ok')
            break
        elif b == 'Bye-Bye':
            print(a)
            c = False
    except KeyboardInterrupt:
        print('Bye-Bye')
        c = False

