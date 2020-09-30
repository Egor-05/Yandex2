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
        if  len(self.args_positional):
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


class LittleBell(Bell):
    def sound(self):
        print("ding")


class BellTower:
    def __init__(self, *args):
        self.bells = []
        for arg in args:
            self.bells.append(arg)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')




Bell("бронзовый").print_info()
LittleBell("медный", нота="ля").print_info()
BigBell(название="Корноухий", вес="1275 пудов").print_info()