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


class BigBell:
    a = 0

    def sound(self):
        if not self.a:
            print('ding')
            self.a = 1
        else:
            print('dong')
            self.a = 0


class LittleBell:
    def sound(self):
        print("ding")


bell_tower = BellTower(BigBell(), LittleBell())
bell_tower.sound()
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()
bell_tower.sound()
bell_tower = BellTower()
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()