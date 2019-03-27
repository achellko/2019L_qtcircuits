from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import *


class DialogTemplate(QDialog):
    def __init__(self, resultData=None):
        super(QDialog, self).__init__()
        self._resultData = resultData
        self.lay = QVBoxLayout()
        self.setLayout(self.lay)
        self.lay.setContentsMargins(0,0,0,0)
        self.w = QWidget()
        p = self.w.palette()
        p.setColor(QPalette.Background, QColor.fromRgb(249, 188, 174, 255))
        self.w.setPalette(p)
        self.w.setAutoFillBackground(True)
        self.w.setVisible(False)
        self.lay.addWidget(self.w)
        lw = QHBoxLayout()
        self.w.setLayout(lw)
        self.lblMessage = QLabel("")
        lw.addWidget(self.lblMessage)
        self.pb = QPushButton("x")
        self.pb.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        lw.addWidget(self.pb)
        self.pb.clicked.connect(self.on_clear)

    def setCentralWidget(self, w):
        self.lay.addWidget(w)

    def error(self, str):
        self.lblMessage.setText(str)
        if str is None or len(str) == 0:
            self.w.setVisible(False)
        else:
            self.w.setVisible(True)

    def on_clear(self):
        self.lblMessage.setText("")
        self.w.setVisible(False)