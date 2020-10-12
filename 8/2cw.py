import sys


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = 0

    def initUI(self):
        self.setGeometry(510, 640, 510, 640)
        self.setWindowTitle('Арифмометр')

        self.btn = QPushButton('Показать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 76)
        self.btn.resize(100, 30)
        self.btn.clicked.connect(self.draw)

        self.inp1 = QLineEdit(self)
        self.inp1.move(350, 26)
        self.inp1.resize(130, 30)

        self.inp2 = QLineEdit(self)
        self.inp2.move(350, 76)
        self.inp2.resize(130, 30)

        self.inp3 = QLineEdit(self)
        self.inp3.move(350, 126)
        self.inp3.resize(130, 30)

        self.label = QLabel(self)
        self.label.setText("side")
        self.label.move(300, 30)

        self.label = QLabel(self)
        self.label.setText("coeff")
        self.label.move(300, 80)

        self.label = QLabel(self)
        self.label.setText("n")
        self.label.move(300, 130)

        self.image = QLabel(self)
        self.image.move(25, 170)
        self.image.resize(450, 450)

    def draw(self):
        img = Image.new("RGB", (450, 450), '#FFFFFF')
        draw = ImageDraw.Draw(img)
        side = int(self.inp1.text())
        for i in range(int(self.inp3.text())):
            x1 = 225 - side / 2
            y1 = 225 - side / 2
            x2 = 225 + side / 2
            y2 = 225 + side / 2
            draw.rectangle((x1, y1, x2, y2), outline='#FF0000')
            side *= float(self.inp2.text())
        img.save('showimg.jpg')
        self.pixmap = QPixmap('showimg.jpg')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())