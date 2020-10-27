import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QStatusBar
from PyQt5.QtWidgets import QLabel, QLineEdit, QTableWidget, QTableWidgetItem
import sqlite3


class Example(QWidget):
    btns = []

    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = 0

    def initUI(self):
        self.setGeometry(1000, 500, 1000, 500)
        self.setWindowTitle('Фокус со словами')

        self.stat = QStatusBar(self)
        self.stat.resize(980, 20)
        self.stat.move(10, 470)

        self.layout = QHBoxLayout()

        ltrs = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        for i in range(len(ltrs)):
            self.btns.append(QPushButton(self))
            self.btns[i].setText(ltrs[i].upper())
            self.btns[i].resize(20, 20)
            self.btns[i].move((i + 1) * 10 + 20 * i, 10)
            self.layout.addWidget(self.btns[i])
            self.btns[i].clicked.connect(self.pressed_ltr)

        self.table = QTableWidget(self)
        self.table.move(10, 50)
        self.table.resize(980, 410)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['ID', 'Название', 'Жанр',
                                                    'Год', 'Продолжительность'])
        self.table.setRowCount(0)
        self.fill_table()

    def pressed_ltr(self):
        a = self.sender().text()
        self.fill_table(a)

    def fill_table(self, ltr=''):
        with sqlite3.connect('films_db.sqlite') as con:
            cur = con.cursor()
            res = cur.execute(f"""SELECT * FROM Films WHERE title like '{ltr}%'""").fetchall()
            self.table.setRowCount(len(res))
            for i, row in enumerate(res):
                for j, elem in enumerate(row):
                    self.table.setItem(
                        i, j, QTableWidgetItem(str(elem)))
            self.table.resizeColumnsToContents()
            if len(res) > 0:
                self.stat.showMessage(f'Нашлось {len(res)} результатов')
            else:
                self.stat.showMessage('К сожалению, ничего не нашлось')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())