from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtWidgets import QWidget


class QtCircuitCanvas(QWidget):
    def __init__(self, *__args):
        super().__init__()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(Qt.blue)
        p.setFont(QFont("Arial", 30))
        p.drawRect(10, 10, 50, 50)
        p.end()
