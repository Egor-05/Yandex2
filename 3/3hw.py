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

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"


class CheckMark:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __bool__(self):
        x1 = self.p1.x
        x2 = self.p2.x
        x3 = self.p3.x
        y1 = self.p1.y
        y2 = self.p2.y
        y3 = self.p3.y
        return x3 * (y2 - y1) - y3 * (x2 - x1) != x1 * y2 - x2 * y1

    def __str__(self):
        return self.p1.name + self.p2.name + self.p3.name

    def __eq__(self, other):
        a1 = len({self.p1.x, other.p1.x})
        a2 = len({self.p1.x, other.p3.x})
        a3 = len({self.p3.x, other.p3.x})
        a4 = len({self.p2.x, other.p2.x})
        b1 = len({self.p1.y, other.p1.y})
        b2 = len({self.p1.y, other.p3.y})
        b3 = len({self.p3.y, other.p3.y})
        b4 = len({self.p2.y, other.p2.y})

        return ((a1 == a3 or a2 == 1) and a4 == 1) and \
               ((b1 == b3 or b2 == 1) and b4 == 1)


T1 = Point('A1', 3, 4)
T2 = Point('A2', 6, 5)
T3 = Point('A3', 5, 2)
T4 = Point('A4', 4, -1)
T5 = Point('A5', 5, 4)
T6 = Point('A6', 5, -1)
T7 = Point('A7', 6, -1)

cm_a = CheckMark(T5, T3, T6)
cm_b = CheckMark(T6, T3, T5)
cm_c = CheckMark(T5, T3, T7)
cm_d = CheckMark(T4, T3, T4)
cm_e = CheckMark(T7, T3, T5)
cm_f = CheckMark(T2, T1, T5)
cm_g = CheckMark(T5, T3, T7)
cm_h = CheckMark(T2, T2, T2)

print(cm_a == cm_b)
print(cm_a == cm_c)
print(cm_a != cm_b)
print(cm_a != cm_c)
print()
print(cm_c == cm_e)
print(cm_c == cm_g)
print(cm_g == cm_e)
print()
print(cm_a == cm_h)
print(cm_a != cm_h)
print(cm_f == cm_h)
print(cm_f != cm_h)
print()
print(cm_h == cm_h)
print(cm_h != cm_h)
print(cm_f == cm_f)
print(cm_f != cm_f)