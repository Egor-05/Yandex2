import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QColor
from ui_1 import Ui_Dialog
import csv
from random import randint


class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable()
        self.pushButton.clicked.connect(self.change_color)

    def loadTable(self):
        with open('price.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title) + 1)
            self.tableWidget.setHorizontalHeaderLabels(title + ['кол-во'])
            self.tableWidget.setRowCount(0)
            self.a = 0
            b = []
            for i in reader:
                b.append(i)
            b.sort(key=lambda x: int(x[1]), reverse=True)
            for i, row in enumerate(b):
                self.a += 1
                row[2] = '0'
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
        self.change_color()
        self.tableWidget.itemChanged.connect(self.change)

    def change(self):
        s = 0
        for i in range(self.a):
            s += int(self.tableWidget.item(i, 2).text()) * int(self.tableWidget.item(i, 1).text())
        self.lineEdit.setText(str(s))

    def change_color(self):
        for i in range(5):
            a = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.item(i, j).setBackground(a)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
