xx, yy = [], []

coords = [input().split(' ') for i in range(int(input()))]

for i in coords:
    if abs(int(i[0])) != abs(int(i[1])) and abs(int(i[0])) > abs(int(i[1])):
        print(f'({i[0]}, {i[1]})')

    xx.append(int(i[0])), yy.append(int(i[1]))

max_x, min_x, max_y, min_y = [max(xx)], [min(xx)], [max(yy)], [min(yy)]

for i in coords:
    if max_x == int(i[0]):
        max_x.append(int(i[1]))

    elif min_x == int(i[0]):
        min_x.append(int(i[1]))

    elif max_y == int(i[1]):
        max_y.insert(0, int(i[0]))

    elif min_y == int(i[1]):
        min_y.insert(0, int(i[0]))

print(f'left: ({min_x[0]}, {min_x[-1]})')
print(f'right: ({max_x[0]}, {max_x[-1]})')
print(f'top: ({max_y[0]}, {max_y[-1]})')
print(f'bottom: ({min_y[0]}, {min_y[-1]})')