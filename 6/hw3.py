ENG = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
RUS = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']


def check_letters(letters, lang):
    for j in lang:
        assert letters not in j


def check_password(password):
    assert len(password) > 8
    assert not (password.isupper() or password.islower() or password.isdigit())
    dig = False
    for i in password:
        if not dig and i.isdigit():
            dig = True
    assert dig
    password = password.lower()
    for i in range(len(password) - 2):
        word = password[i:i + 3]
        check_letters(word, ENG)
        check_letters(word, RUS)
    return 'ok'


try:
    print(check_password(input()))
except Exception as ex:
    print('error')
