import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QTextEdit, QPushButton


class Example(QWidget):

    lst = []

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(375, 400, 375, 400)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.cb = QCheckBox('Чизбургер', self)
        self.cb.move(20, 40)
        self.cb.stateChanged.connect(lambda: self.ap(self.cb, foodname='Чизбургер'))

        self.cb1 = QCheckBox('Гамбургер', self)
        self.cb1.move(20, 80)
        self.cb1.stateChanged.connect(lambda: self.ap(self.cb1, foodname='Гамбургер'))

        self.cb2 = QCheckBox('Кока-кола', self)
        self.cb2.move(20, 120)
        self.cb2.stateChanged.connect(lambda: self.ap(self.cb2, foodname='Кока-кола'))

        self.cb3 = QCheckBox('Нагетсы', self)
        self.cb3.move(20, 160)
        self.cb3.stateChanged.connect(lambda: self.ap(self.cb3, foodname='Нагетсы'))

        self.te = QTextEdit(self)
        self.te.setReadOnly(True)
        self.te.move(20, 220)

        self.btn = QPushButton('Заказать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(20, 190)
        self.btn.clicked.connect(self.print_check)

    def ap(self, cb, foodname):
        if cb.isChecked():
            self.lst.append(foodname)
        else:
            if foodname in self.lst:
                del self.lst[self.lst.index(foodname)]

    def print_check(self):
        self.te.clear()
        self.te.append('Ваш заказ:\n')
        for i in self.lst:
            self.te.append(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())