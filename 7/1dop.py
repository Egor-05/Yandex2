with open('pipes.txt', 'r') as f:
    lst = f.read().splitlines()
del lst[-2]
workers = [int(i) for i in lst[-1].split()]
pipes = {}
for i in range(len(lst) - 1):
    pipes[i + 1] = float(lst[i])
res = 1
s = 0
for i in workers:
    s += 1 / pipes[i]
res /= s
res *= 60
f1 = open('time.txt', 'w')
f1.write(str(res))
