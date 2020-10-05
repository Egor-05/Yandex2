a = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
     "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
     "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
     "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
     "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
     "б": "b", "ю": "ju", "ё": "jo"}


with open('cyrillic.txt', 'r') as f:
    b = f.read().splitlines()
b = '\n'.join(b)
res = ''
for i in b:
    if i.lower() in list(a.keys()):
        if i.isupper():
            res += a[i.lower()].capitalize()
        else:
            res += a[i.lower()]
    else:
        res += i
print(res)
with open('transliteration.txt', 'w') as f:
    f.write(res)
