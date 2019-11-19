import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget

SCREEN_SIZE = [400, 400]


class Circles(QWidget):
    def __init__(self):
        self.init = True
        super().__init__()
        uic.loadUi('Ui.ui',self)
        self.initUi()

    def initUi(self):
        self.setGeometry(400, 200, *SCREEN_SIZE)

        self.pushButton.clicked.connect(self.redraw)

    def redraw(self):
        self.init = False
        self.repaint()
        self.init = True

    def paintEvent(self, event):
        if self.init:
            return None
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        qp.setBrush(Qt.yellow)
        qp.drawEllipse(randint(0, SCREEN_SIZE[0]),
                      randint(50, SCREEN_SIZE[1]), *(randint(1, 100),) * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
