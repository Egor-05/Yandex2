import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_4 import Ui_Dialog
import csv


class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.itemsforcombobox = ['Все']
        self.itemsforcombobox_2 = ['Все']
        self.logins = []
        self.loadNewCsv()
        self.comboboxes_filling()
        self.pushButton.clicked.connect(self.change)

    def comboboxes_filling(self):
        for i in self.itemsforcombobox:
            self.comboBox.addItem(i)
        for i in self.itemsforcombobox_2:
            self.comboBox_2.addItem(i)

    def loadNewCsv(self):
        with open('rez.csv', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            students = []
            for i in reader:
                a = i['login'].split('-')
                if a[2] not in self.itemsforcombobox:
                    self.itemsforcombobox.append(a[2])
                if a[3] not in self.itemsforcombobox_2:
                    self.itemsforcombobox_2.append(a[3])
                self.logins.append([a[2], a[3]])
                students.append([i['user_name'].split()[3], i['Score']])
            students.sort(key=lambda x: x[0], reverse=True)
            students.sort(key=lambda x: int(x[1]), reverse=True)
            with open('result.csv', 'w') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(['Фамилия', 'Результат'])
                writer.writerows(students)

    def change(self):
        with open('result.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            c = 0
            for i, row in enumerate(reader):
                a = self.comboBox.currentText()
                b = self.comboBox_2.currentText()
                if self.logins[i] == [a, b] or (a == 'Все' and self.logins[i][1] == b) or \
                   (b == 'Все' and self.logins[i][0] == a) or a == b == 'Все':
                    self.tableWidget.insertRow(c)
                    self.tableWidget.setItem(c, 0, QTableWidgetItem(row[0]))
                    self.tableWidget.setItem(c, 1, QTableWidgetItem(row[1]))
                    c += 1


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
