class Cinema:
    def __init__(self):
        self.lst = []

    def append_zal(self, width, length, num, rasp):
        self.lst.append(Zal(width, length, num, rasp))


class Zal:
    def __init__(self, width, length, num, rasp):
        self.num = num
        self.matrix = [[0 for i in range(width)] for j in range(length)]
        self.rasp = {}
        for i in rasp:
            self.rasp[i] = self.matrix

    def find_places_in_a_row(self, num, nametime):
        lst = []
        a = self.rasp[nametime]
        for i in range(len(a)):
            for j in range(len(a[i])):
                if j + num < len(a[i]):
                    b = []
                    for e in range(j, j + num + 1):
                        if a[i][e] == 0:
                            b.append((e, i))
                    if len(b) == num:
                        lst.append(b)
        if len(lst) > 0:
            print(f'{num} мест в ряд в зале {self.num} есть в наличии')
        else:
            print(f'{num} мест в ряд в зале {self.num} нет в наличии')

    def buy_place(self, x, y, nametime):
        self.rasp[nametime][x][y] = 1

    def add_film(self, name, rasp, length):




class Film:
    def __init__(self, name, rasp, length, n, m):
        self.name = name
        self.rasp = rasp
        self.length = length

