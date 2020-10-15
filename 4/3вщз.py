import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QTextEdit, QPushButton, QLineEdit


class Example(QWidget):

    lst = []

    def __init__(self):
        super().__init__()

        self.initUI()
        self.dct = {'Чизбургер': [10, self.te1], 'Гамбургер': [20, self.te2],
                    'Кока-кола': [30, self.te3], 'Нагетсы': [40, self.te4]}

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

        self.te1 = QLineEdit(self)
        self.te1.setText('0')
        self.te1.resize(50, 20)
        self.te1.move(120, 40)
        self.te1.hide()

        self.te2 = QLineEdit(self)
        self.te2.setText('0')
        self.te2.resize(50, 20)
        self.te2.move(120, 80)
        self.te2.hide()

        self.te3 = QLineEdit(self)
        self.te3.setText('0')
        self.te3.resize(50, 20)
        self.te3.move(120, 120)
        self.te3.hide()

        self.te4 = QLineEdit(self)
        self.te4.setText('0')
        self.te4.resize(50, 20)
        self.te4.move(120, 160)
        self.te4.hide()

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
            self.dct[foodname][1].show()
            self.dct[foodname][1].setText('1')
        else:
            if foodname in self.lst:
                del self.lst[self.lst.index(foodname)]
            self.dct[foodname][1].hide()
            self.dct[foodname][1].setText('2')

    def print_check(self):
        self.te.clear()
        self.te.append('Ваш заказ:\n')
        s = 0
        for i in self.lst:
            a = self.dct[i]
            b = int(a[1].text()) * a[0]
            self.te.append(f'{i}-----{a[1].text()}-----{b}')
            s += b
        self.te.append(f'Итого: {s}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())