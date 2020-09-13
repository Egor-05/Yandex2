import sys


daleki = ['далек',
          'далека',
          'далеку',
          'далеком',
          'далеке',
          'далеки',
          'далеков',
          'далекам',
          'далеками',
          'далеках']
s = 0
for i in sys.stdin:
    a = i.split()
    for j in a:
        if j.lower() in daleki:
            s += 1
            break
print(s)