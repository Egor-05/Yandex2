Cinemas = []
Films = []


class Cinema:
    def __init__(self):
        self.lst = []
        self.num = len(Cinemas)

    def append_zal(self, width, length):
        self.lst.append(Zal(width, length, ))


class Zal:
    def __init__(self, col, row):
        self.col = col
        self.row = row


class Film:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.seanses = []

    def add_seans(self, start_time, cinema_idx, zal_idx):
        self.seanses.append(Seans(start_time, cinema_idx, zal_idx))

    def find_nearest_seans(self):
        time = []
        for i in self.seanses:
            time1 = i.start_time.split(':')
            if len(time) == 0 or time[0] > time1[0] or \
               (time[0] == time1[0] and time[1] > time1[1]):
                for j in i.places:
                    if False in j:
                        time = time1
                        s = i
                        break
        if len(time) > 0:
            return s
        else:
            print(f'На сегодняшний день места на '
                  f'показ фильма {self.name} отсутствуют')

    def show_seans(self, seans):
        time = seans.start_time.split(':')

        print(f'Кинотеатр № {seans.cinema_idx + 1}')
        print(f'Зал № {seans.zal_idx + 1}')
        print(f'Время - {":".join(time)}')
        print('[ ] - место свободно\n[#] - место занято')
        for i in seans.places:
            print(''.join(['[#]' if j else '[ ]' for j in i]))


class Seans:
    def __init__(self, start_time, cinema_idx, zal_idx):
        self.start_time = start_time
        self.cinema_idx = cinema_idx
        self.zal_idx = zal_idx
        a = Cinemas[cinema_idx].lst[zal_idx]
        self.places = [[False for i in range(a.row)] for j in range(a.col)]

    def get_place_status(self, x, y):
        x -= 1
        y -= 1
        return self.places[y][x]

    def buy_place(self, x, y):
        x -= 1
        y -= 1
        if not self.places[y][x]:
            self.places[y][x] = True
            return True
        return False


Cinemas.append(Cinema())
Cinemas[0].append_zal(6, 6)
Films.append(Film("Homa's adventures", 60))
Films[0].add_seans('12:00', 0, 0)
print('Успешно' if Films[0].seanses[0].buy_place(3, 3) else 'Место занято, выберите другое')
a = Films[0].find_nearest_seans()
Films[0].show_seans(a)
