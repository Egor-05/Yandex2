with open('prices.txt', 'r') as f:
    lst = f.readlines()
if len(lst) > 0:
    res = 0
    for i in lst:
        i = i.strip('\n').split('\t')
        res += float(i[2]) * float(i[1])
    print(res)
else:
    print(0)