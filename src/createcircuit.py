from PyQt5.QtWidgets import *
from cirapp import tr
from dialogtemplate import DialogTemplate


class CircuitCreateAction(QAction):
    def __init__(self, *__args):
        super().__init__(tr("Nowy schemat"))

        self.triggered.connect(self.on_create)

    def on_create(self):
        res = {}
        dlg = QNewCircuitDialog(res)
        r = dlg.exec()
        if r == QDialog.Accepted:
            print(f"Zaakceptowano i podano nazwę: {res['newCircuitName']}")


class QNewCircuitDialog(DialogTemplate):
    def __init__(self, resultData=None):
        super(QNewCircuitDialog, self).__init__(resultData)
        self.setWindowTitle("Utwórz nowy schemat")
        w = QWidget(self)
        w.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(w)
        lay = QGridLayout()
        w.setLayout(lay)
        lay.addWidget(QLabel("Nazwa schematu"), 0, 0)
        self.txtName = QLineEdit()
        lay.addWidget(self.txtName, 0, 1)
        lv = QHBoxLayout()
        lay.addLayout(lv, 1, 1)
        lv.addStretch()
        cmdAdd = QPushButton(tr("Dodaj"))
        cmdAdd.clicked.connect(self.on_add)
        lv.addWidget(cmdAdd)
        cmdCancel = QPushButton(tr("Anuluj"))
        cmdCancel.clicked.connect(self.on_cancel)
        lv.addWidget(cmdCancel)

    def on_add(self):
        if len(self.txtName.text()) == 0:
            self.error(tr("Proszę podać nazwę schematu, lub użyć komendy Anuluj."))
        else:
            self._resultData["newCircuitName"] = self.txtName.text()
            self.accept()

    def on_cancel(self):
        self.reject()