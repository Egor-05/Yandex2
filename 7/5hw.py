import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton


class Example(QWidget):

    lst = []

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setGeometry(300, 250, 300, 250)
        self.setWindowTitle('Перемешивание')

        self.btn = QPushButton(self)
        self.btn.setText('Загрузить строки')
        self.btn.resize(120, 20)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.print_check)

        self.te = QTextEdit(self)
        self.te.setReadOnly(True)
        self.te.move(20, 50)


    def print_check(self):
        self.te.clear()
        self.te.append(res)


with open('input.txt', 'r') as f:
    lst = f.read().splitlines()
res = ''
for i in range(1, len(lst), 2):
    res += lst[i] + '\n'
for i in range(0, len(lst), 2):
    res += lst[i] + '\n'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
