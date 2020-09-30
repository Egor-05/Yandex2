import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QTextEdit, QPushButton, QLineEdit


class Example(QWidget)
    lst = []

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(375, 400, 375, 400)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.menu = {1: ['Чизбургер', self.quant1],
                     2: ['Гамбургер', self.quant2],
                     3: ['Кока-кола', self.quant3],
                     4: ['Нагетсы', self.quant4]}
        self.cb1 = QCheckBox('Чизбургер', self)
        self.cb1.move(20, 40)
        self.cb1.stateChanged.connect(lambda: self.ap(self.cb1, foodname='Чизбургер'))
        self.quant1 = QLineEdit(self)
        self.quant1.resize(50, 20)

        self.cb2 = QCheckBox('Гамбургер', self)
        self.cb2.move(20, 80)
        self.cb2.stateChanged.connect(lambda: self.ap(self.cb2, foodname='Гамбургер'))

        self.cb3 = QCheckBox('Кока-кола', self)
        self.cb3.move(20, 120)
        self.cb3.stateChanged.connect(lambda: self.ap(self.cb3, foodname='Кока-кола'))

        self.cb4 = QCheckBox('Нагетсы', self)
        self.cb4.move(20, 160)
        self.cb4.stateChanged.connect(lambda: self.ap(self.cb4, foodname='Нагетсы'))

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