from PyQt5.QtWidgets import QAction

from createcircuit import CircuitCreateAction
import cirapp
from cirapp import tr


class CircuitsActions(object):
    def __init__(self):
        self.actions = {}
        self.actions["create-circuit"] = CircuitCreateAction()
        self.actions["close-app"] = QAction(tr("Zamknij"))
        self.actions["close-app"].triggered.connect(self.on_close)

    # noinspection PyMethodMayBeStatic
    def on_close(self):
        cirapp.get_app().exit(0)
