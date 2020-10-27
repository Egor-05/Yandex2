ENG = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
RUS = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']


def check_letters(letters, lang):
    for j in lang:
        if letters in j:
            return True
    return False


def error1(password):
    dig = False
    for i in password:
        if not dig and i.isdigit():
            dig = True
    if not dig:
        raise DigitError


def error2(password):
    if len(password) <= 8:
        raise LengthError


def error3(password):
    if password.isupper() or password.islower() or password.isdigit() or not password.isalnum():
        raise LetterError


def error4(password):
    for i in range(len(password) - 2):
        word = password.lower()[i:i + 3]
        if not check_letters(word, ENG):
            if check_letters(word, RUS):
                raise SequenceError
        else:
            raise SequenceError


def error5(password):
    for i in words:
        if i in password.lower():
            raise WordError


def check_password(password, func):
    try:
        func(password)
    except DigitError:
        errors[0] += 1
    except LengthError:
        errors[1] += 1
    except LetterError:
        errors[2] += 1
    except SequenceError:
        errors[3] += 1
    except WordError:
        errors[4] += 1


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


class WordError(PasswordError):
    pass


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
    for j in [error1, error2, error3, error4, error5]:
        check_password(i, j)
for i in range(5):
    print(f'{types_errors[i]} - {errors[i]}')
