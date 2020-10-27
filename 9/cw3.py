import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_1 import Ui_Dialog
import csv


class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable()

    def loadTable(self):
        with open('price.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title) + 1)
            self.tableWidget.setHorizontalHeaderLabels(title + ['кол-во'])
            self.tableWidget.setRowCount(0)
            self.a = 0
            for i, row in enumerate(reader):
                self.a += 1
                row[2] = '0'
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))

        self.tableWidget.itemChanged.connect(self.change)

    def change(self):
        s = 0
        for i in range(self.a):
            s += int(self.tableWidget.item(i, 2).text()) * int(self.tableWidget.item(i, 1).text())
        self.lineEdit.setText(str(s))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
