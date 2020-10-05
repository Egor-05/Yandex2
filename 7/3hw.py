def palindrome():
    with open('input.dat', 'rb') as f:
        b = f.read()
    return b == b[::-1]