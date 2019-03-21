# coding=utf8
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
import os

def tr(s):
    return app.translate("@default",s)

class CircuitsLists(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setLayout(QVBoxLayout())
        self.list = QListWidget()
        self.layout().addWidget(self.list)
        self.list.addItem(tr("(Kliknij dodaj nowy)"))


class Welcome(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setLayout(QGridLayout())
        lbl = QLabel(tr("Witamy w przyjaznej aplikacji "
                     "do rysowania schematow elektrycznych."))
        self.layout().addWidget(lbl, 0, 0)
        self.web = QWebEngineView()
        self.layout().addWidget(self.web, 2, 0)
        start = tr("start.html")
        startFile = f"{os.path.dirname(os.path.realpath(__file__))}/{start}"
        self.web.load(QUrl(f"file:{startFile}"))





class CircuitsEditors(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setLayout(QVBoxLayout())
        self.tabs = QTabWidget()
        self.layout().addWidget(self.tabs)
        self.tabs.addTab(Welcome(), tr("Witaj!"))

app = QApplication([])

translator = QTranslator()
translator.load(QLocale(), "qtcircuits", "_", os.path.dirname(os.path.realpath(__file__)))
print(app.installTranslator(translator))

mw = QMainWindow()
mw.setWindowTitle(tr("QtCircuit (C) PW GUI Course (Step 1)"))
dockList = QDockWidget(tr("Lista projektow"), mw)
mw.addDockWidget(Qt.LeftDockWidgetArea, dockList)
dockList.setWidget(CircuitsLists())
mw.setCentralWidget(CircuitsEditors())
mw.show()
app.exec_()