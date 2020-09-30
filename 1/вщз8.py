from random import choice


FIELD_SIZE = 2


def end_print():
    for i in field:
        print(''.join(['[*]' if j else '[#]' for j in i]))


def check_win():
    for i in range(len(field)):
        for j in range(len(field[i])):
            if not field[i][j] and [j, i] not in selected_cells:
                return False
    print('Победа!')
    return True


def get_point():
    print(f'Введите координаты (x, y) клетки через пробел, считая с 1 и до {FIELD_SIZE}:')
    a = [int(i) - 1 for i in input().split()]
    while a in selected_cells or (0 > a[0] or a[0] > FIELD_SIZE - 1 or
                                  0 > a[1] or a[1] > FIELD_SIZE - 1):
        print('Пожалуйста введите координаты точки ещё раз:')
        a = [int(i) - 1 for i in input().split()]
    return a


def bombs_near_cell(x, y):
    d1 = [[x + 1, y + 1],
          [x - 1, y + 1],
          [x + 1, y - 1],
          [x - 1, y - 1],
          [x + 1, y],
          [x - 1, y],
          [x, y + 1],
          [x, y - 1]]
    d = []
    for i in d1:
        if -1 < i[0] < FIELD_SIZE and -1 < i[1] < FIELD_SIZE:
            d.append(i)
    return [field[i[0]][i[1]] for i in d]


def bombs_near_fields():
    e = []
    for i in range(FIELD_SIZE):
        e.append([bombs_near_cell(i, j).count(True) for j in range(FIELD_SIZE)])
    return e


def fill_field(excluded_point):
    return [[choice([True, False]) if [j, i] != excluded_point else False
             for j in range(FIELD_SIZE)] for i in range(FIELD_SIZE)]


def visualise_field():
    for y in range(FIELD_SIZE):
        e = []
        for x in range(FIELD_SIZE):
            if [x, y] in selected_cells:
                e.append('[' + str(number_bombs[x][y]) + ']')
            else:
                e.append('[?]')
        print(''.join(e))


selected_cells = []
visualise_field()
a = get_point()
field = fill_field(a)
number_bombs = bombs_near_fields()
selected_cells.append(a)
end_game = check_win()
while not end_game:
    visualise_field()
    a = get_point()
    selected_cells.append(a)
    if field[a[0]][a[1]]:
        print('Поражение!')
        end_game = True
    else:
        end_game = check_win()

print('* - бомба')
print('# - пустая клетка')
end_print()