import sys
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    value = 1

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(410, 360, 410, 360)
        self.setWindowTitle('QSlider')

        sld = QSlider(self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 30, 20, 200)
        sld.move(380, 20)
        sld.setValue(50)
        sld.valueChanged[int].connect(self.changeValue)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawSmile(qp)
        qp.end()


    def drawSmile(self, qp):
        qp.setPen(QColor(255, 0, 0))
        a = self.value
        qp.drawEllipse(0, 0, 350 * a, 350 * a)
        qp.drawEllipse(50 * a, 50 * a, 100 * a, 100 * a)
        qp.drawEllipse(200 * a, 50 * a, 100 * a, 100 * a)
        qp.drawArc(50 * a, 150 * a, 250 * a, 150 * a, 0 * 16, -180 * 16)

    def draw(self):
        self.update()

    def changeValue(self, value):
        self.value = value / 50
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())