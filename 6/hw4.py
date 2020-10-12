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


run = True
while run:
    try:
        a = input()
        if a == 'Ctrl+Break':
            raise KeyboardInterrupt
        try:
            print(check_password(a))
            run = False
        except LengthError:
            print('LengthError')
        except LetterError:
            print('LetterError')
        except DigitError:
            print('DigitError')
        except SequenceError:
            print('SequenceError')
    except KeyboardInterrupt:
        print('Bye-bye')
        break
