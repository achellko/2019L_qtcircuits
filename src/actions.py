from PyQt5.QtWidgets import QAction

import cirapp
from cirapp import tr


class CircuitsActions(object):
    def __init__(self):
        self.actions = {}
        self.actions["create-circuit"] = QAction(tr("Zamknij"))
        self.actions["create-circuit"].triggered.connect(self.on_close)

    # noinspection PyMethodMayBeStatic
    def on_close(self):
        cirapp.get_app().exit(0)
