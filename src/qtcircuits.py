# coding=utf8
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
import os

import cirapp
from canvasexample import QtCircuitCanvas
from cirapp import tr
from actions import CircuitsActions


class CircuitsLists(QWidget):
    def __init__(self):
        super(CircuitsLists, self).__init__()
        self.setLayout(QVBoxLayout())
        self.list = QListWidget()
        self.layout().addWidget(self.list)
        self.list.addItem(tr("(Kliknij dodaj nowy)"))


class Welcome(QWidget):
    def __init__(self):
        super(Welcome, self).__init__()
        self.setLayout(QGridLayout())
        lbl = QLabel(tr("Witamy w przyjaznej aplikacji "
                     "do rysowania schematow elektrycznych."))
        self.layout().addWidget(lbl, 0, 0)
        self.web = QWebEngineView()
        self.layout().addWidget(self.web, 2, 0)
        start = tr("start.html")
        startFile = f"{os.path.dirname(os.path.realpath(__file__))}/resources/{start}"
        self.web.load(QUrl(f"file:{startFile}"))


class CircuitsEditors(QWidget):
    def __init__(self):
        super(CircuitsEditors, self).__init__()
        self.setLayout(QVBoxLayout())
        self.tabs = QTabWidget()
        self.layout().addWidget(self.tabs)
        self.tabs.addTab(Welcome(), tr("Witaj!"))
        self.tabs.addTab(QtCircuitCanvas(), tr("Przykład płótno!"))

def create_menu(mw, actions):
    mainbar = mw.menuBar()
    # mFile = QMenu(tr("Plik"), mainbar)
    # mainbar.addMenu(mFile)
    mFile = mainbar.addMenu(tr("Plik"))
    mFile.addAction(actions.actions.get("create-circuit"))
    mFile.addAction(actions.actions.get("close-app"))

# app = QApplication([])
app = cirapp.init()
translator = QTranslator()
print(translator.load(QLocale(), "translations/qtcircuits", "_", os.path.dirname(os.path.realpath(__file__))))
print(app.installTranslator(translator))

mw = QMainWindow()
mw.setWindowTitle(tr("QtCircuit (C) PW GUI Course (Step 1)"))
dockList = QDockWidget(tr("Lista projektow"), mw)
mw.addDockWidget(Qt.LeftDockWidgetArea, dockList)
dockList.setWidget(CircuitsLists())
mw.setCentralWidget(CircuitsEditors())

actions = CircuitsActions()
create_menu(mw, actions)

mw.show()
app.exec_()