# coding=utf8
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class CircuitsLists(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setLayout(QVBoxLayout())
        self.list = QListWidget()
        self.layout().addWidget(self.list)
        self.list.addItem("(Kliknij dodaj nowy)")
class Welcome(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setLayout(QGridLayout())
        lbl = QLabel("Witamy w przyjaznej aplikacji "
                     "do rysowania schematów elektrycznych.")
        self.layout().addWidget(lbl, 0, 0)
class CircuitsEditors(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setLayout(QVBoxLayout())
        self.tabs = QTabWidget()
        self.layout().addWidget(self.tabs)
        self.tabs.addTab(Welcome(), "Witaj!")
app = QApplication([])
mw = QMainWindow()
mw.setWindowTitle("QtCircuit (C) PW GUI Course (Step 1)")
dockList = QDockWidget("Lista projektow", mw)
mw.addDockWidget(Qt.LeftDockWidgetArea, dockList)
dockList.setWidget(CircuitsLists())
mw.setCentralWidget(CircuitsEditors())
mw.show()
app.exec_()