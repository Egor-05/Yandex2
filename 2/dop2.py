class Bell:
    def __init__(self, *args1, **args2):
        self.args_positional = []
        for arg in args1:
            self.args_positional.append(arg)
        self.args_named = {arg: args2[arg] for arg in sorted(args2)}

    def print_info(self):
        result = ''


        print(result)


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