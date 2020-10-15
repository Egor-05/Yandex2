import sys


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QButtonGroup, QStatusBar


class Example(QWidget):
    btns = []
    btn_text_X = True
    field = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
    s = 0
    win = False

    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = 0

    def initUI(self):
        self.setGeometry(340, 240, 240, 340)
        self.setWindowTitle('Фокус со словами')

        self.rb1 = QRadioButton(self)
        self.rb1.setText('X')
        self.rb1.move(85, 20)
        self.rb1.setChecked(True)

        self.rb2 = QRadioButton(self)
        self.rb2.setText('O')
        self.rb2.move(125, 20)

        self.bg = QButtonGroup(self)
        self.bg.addButton(self.rb1)
        self.bg.addButton(self.rb2)
        self.bg.buttonClicked.connect(self.check)


        self.stat = QStatusBar(self)
        self.stat.resize(100, 30)
        self.stat.move(100, 260)

        self.btn = QPushButton(self)
        self.btn.setText('Новая игра')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 300)
        self.btn.clicked.connect(self.new_game)

        x = -50
        y = -20
        for j in range(9):
            x = -50 if j % 3 == 0 else x
            if j % 3 == 0:
                y += 70
            x += 70
            self.btns.append(QPushButton(self))
            self.btns[j].setText('')
            self.btns[j].resize(60, 60)
            self.btns[j].move(x, y)
            self.btns[j].clicked.connect(self.btn_ispressed)

    def btn_ispressed(self):
        a = self.sender()
        if self.s < 9 and a.text() == '' and not self.win:
            b = self.btns.index(a)
            c = 'X' if self.btn_text_X else 'O'
            a.setText(c)
            self.field[b // 3][b % 3] = c.lower()
            self.s += 1
            self.check_win()
            self.btn_text_X = not self.btn_text_X

    def check(self):
        if self.s == 0:
            self.btn_text_X = self.rb1.isChecked()

    def check_win(self):
        for i in range(3):
            s = ''.join([self.field[i][j] for j in range(3)])
            if 'ooo' in s:
                self.stat.showMessage('Выйграл O!')
                self.win = True
            elif 'xxx' in s:
                self.stat.showMessage('выйграл X!')
                self.win = True
        for i in range(3):
            s = ''.join([self.field[j][i] for j in range(3)])
            if 'ooo' in s:
                self.stat.showMessage('Выйграл O!')
                self.win = True
            elif 'xxx' in s:
                self.stat.showMessage('Выйграл X!')
                self.win = True
        if self.field[0][0] + self.field[1][1] + self.field[2][2] == 'xxx':
            self.stat.showMessage('Выйграл X!')
            self.win = True
        elif self.field[0][0] + self.field[1][1] + self.field[2][2] == 'ooo':
            self.stat.showMessage('Выйграл O!')
            self.win = True
        elif self.field[0][2] + self.field[1][1] + self.field[2][0] == 'xxx':
            self.stat.showMessage('Выйграл X!')
            self.win = True
        elif self.field[2][0] + self.field[1][1] + self.field[2][0] == 'ooo':
            self.stat.showMessage('Выйграл O!')
            self.win = True
        if self.s == 9:
            self.stat.showMessage('Ничья!')

    def new_game(self):
        self.btn_text_X = True
        self.field = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.s = 0
        self.win = False
        for i in range(len(self.btns)):
            self.btns[i].setText('')
            self.stat.showMessage('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())