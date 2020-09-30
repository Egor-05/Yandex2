from itertools import product


class Bell:
    def __init__(self, *args, **kwargs):
        self.args_positional = []
        for arg in args:
            self.args_positional.append(arg)
        self.args_named = {arg: kwargs[arg] for arg in sorted(kwargs)}

    def print_info(self):
        result = ''
        for i in self.args_named:
            result += f'{i}: {self.args_named[i]}, '
        if result != '' and len(self.args_positional):
            result = result[:-2] + '; '
        elif not len(self.args_positional):
            result = result[:-2]
        for i in self.args_positional:
            result += f'{i}, '
        if len(self.args_positional):
            result = result[:-2]
        print(result.strip() if result != '' else '-')


class BigBell(Bell):
    a = 0

    def sound(self):
        if not self.a:
            print('ding')
            self.a = 1
        else:
            print('dong')
            self.a = 0

    def name(self):
        return 'BigBell'


class LittleBell(Bell):
    def sound(self):
        print("ding")

    def name(self):
        return 'LittleBell'


class BellTower:

    def __init__(self, *args):
        self.bells = []
        for i in args:
            if type(i) not in [tuple, list]:
                i = [i]
            for j in i:
                self.bells.append(j)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')

    def print_info(self):
        for i in range(len(self.bells)):
            print(f'{i + 1} {self.bells[i].name()}')
            self.bells[i].print_info()
        print()


class SizedBellTower(BellTower):
    def __init__(self, *args, size=10):
        super().__init__(args)
        self.size = size
        if len(self.bells) > size:
            self.bells = self.bells[len(self.bells) - size:]

    def append(self, bell):
        if len(self.bells) < self.size:
            self.bells.append(bell)
        else:
            self.bells = self.bells[1:]
            self.bells.append(bell)


class TypedBellTower(BellTower):
    def __init__(self, *args, bell_type=LittleBell):
        super().__init__(args)
        self.b_t = 'LittleBell' if bell_type == LittleBell else 'BigBell'
        self.cleaner()

    def cleaner(self):
        a = self.bells.copy()
        self.bells.clear()
        for i in a:
            if i.name() == self.b_t:
                self.bells.append(i)

    def append(self, bell):
        if bell.name() == self.b_t:
            self.bells.append(bell)


bells = [BigBell(), BigBell("медный"), BigBell(цвет="серебристый"), BigBell("звонкий", диаметр="5 см"), BigBell("ля"),
         LittleBell("звонкий"), LittleBell(нота="до"), LittleBell(),
         LittleBell("тихий", "мелодичный", вес="100 грамм", нота="ре"), LittleBell()]
bt_default = SizedBellTower(*bells)
bt_1 = SizedBellTower(*bells, size=1)
bt_2 = SizedBellTower(*bells, size=2)
bt_10 = SizedBellTower(*bells, size=10)
bt_11 = SizedBellTower(*bells, size=11)
bt_20 = SizedBellTower(*bells, size=20)
bts = [bt_default, bt_1, bt_2, bt_10, bt_11, bt_20]

bb = BigBell("самый звонкий")
lb = LittleBell("самый маленький")
for bt in bts:
    bt.append(bb)
    bt.append(lb)
for bt in bts:
    bt.print_info()