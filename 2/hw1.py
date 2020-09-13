class Point:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.x, self.y)

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'

    def __invert__(self):
        return Point(self.name, self.y, self.x)


P1 = Point('p1', 37, 766545)
P2 = Point('p2',  1223, -5543)
P3 = Point('p3', -11111111111, 44444444444444)
P4 = ~P1
P5 = ~P3
P6 = ~P2
print(P1, P2, P3, P4, P5, P6)

P7 = ~P6
P8 = ~P5
P9 = ~P4
print(P7, P8, P9)

if P1.get_x() == P9.get_x() and P1.get_y() == P9.get_y():
    print("yes")
else:
    print("no")
if P2.get_x() == P7.get_x() and P7.get_y() == P2.get_y():
    print("yes")
else:
    print("no")
if P8.get_x() == P5.get_x() and P8.get_y() == P5.get_y():
    print("yes")
else:
    print("no")
if P8.get_x() == P3.get_x() and P8.get_y() == P3.get_y():
    print("yes")
else:
    print("no")