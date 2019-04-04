from PyQt5.QtWidgets import QAction

from createcircuit import CircuitCreateAction
import cirapp
from cirapp import tr

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os

import cirapp
from cirapp import tr


class CircuitsActions(object):
    def __init__(self):
        self.actions = {}
        self.actions["create-circuit"] = CircuitCreateAction()
        self.actions["close-app"] = QAction(tr("Zamknij"))
        self.actions["close-app"].triggered.connect(self.on_close)

        self.actions["polski"] = QAction(tr("Polski"))
        self.actions["polski"].triggered.connect(self.trans_pl)

        self.actions["english"] = QAction(tr("English"))
        self.actions["english"].triggered.connect(self.trans_en)


    # noinspection PyMethodMayBeStatic
    def on_close(self):
        cirapp.get_app().exit(0)

    def trans_pl(self):
        translator = cirapp.get_translator()
        cirapp.get_app().removeTranslator(translator)
        translator = QTranslator()
        translator.load(QLocale(), "qtcircuits_pl.qm")
        print(cirapp.get_app().installTranslator(translator))

        msgBox = QMessageBox()
        msgBox.setText(tr("Witaj!"))
        msgBox.exec()

    def trans_en(self):
        translator = cirapp.get_translator()
        cirapp.get_app().removeTranslator(translator)
        translator = QTranslator()
        translator.load(QLocale(), "qtcircuits_en.qm")
        print(cirapp.get_app().installTranslator(translator))

        msgBox = QMessageBox()
        msgBox.setText(tr("Witaj!"))
        msgBox.exec()
