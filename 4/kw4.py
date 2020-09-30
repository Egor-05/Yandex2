import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLineEdit
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(375, 200, 375, 200)
        self.setWindowTitle('Прятки для виджетов')

        cb = QCheckBox('edit1', self)
        cb.move(20, 40)
        cb.toggle()
        cb.stateChanged.connect(self.sh1)

        self.name_input = QLineEdit(self)
        self.name_input.move(100, 40)
        self.name_input.setText('Поле edit1')

        cb1 = QCheckBox('edit2', self)
        cb1.move(20, 80)
        cb1.toggle()
        cb1.stateChanged.connect(self.sh2)

        self.name_input1 = QLineEdit(self)
        self.name_input1.move(100, 80)
        self.name_input1.setText('Поле edit2')

        cb2 = QCheckBox('egit3', self)
        cb2.move(20, 120)
        cb2.toggle()
        cb2.stateChanged.connect(self.sh3)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(100, 120)
        self.name_input2.setText('Поле edit3')

        cb3 = QCheckBox('edit4', self)
        cb3.move(20, 160)
        cb3.toggle()
        cb3.stateChanged.connect(self.sh4)

        self.name_input3 = QLineEdit(self)
        self.name_input3.move(100, 160)
        self.name_input3.setText('Поле edit4')

    def sh1(self, state):
        if state == Qt.Checked:
            self.name_input.show()
        else:
            self.name_input.hide()

    def sh2(self, state):
        if state == Qt.Checked:
            self.name_input1.show()
        else:
            self.name_input1.hide()

    def sh3(self, state):
        if state == Qt.Checked:
            self.name_input2.show()
        else:
            self.name_input2.hide()

    def sh4(self, state):
        if state == Qt.Checked:
            self.name_input3.show()
        else:
            self.name_input3.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())