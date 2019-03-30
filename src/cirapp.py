from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication
from circuitsmodel import CircuitsStore
import os


def tr(s):
    return _app.translate("@default", s)


def init():
    global _app
    _app = QApplication([])

    appath = os.path.dirname(__file__)

    font_path = os.path.join(appath, "resources", "FontAwesome.otf")
    res = QFontDatabase.addApplicationFont(font_path)
    if res == -1:
        print(f"Błąd podczas wczytywania czcionki Awesome z lokalizacji: {font_path}")

    global _font_awesome
    _font_awesome = QFont()
    _font_awesome.setFamily("Font Awesome 5 Free")

    store_path = os.path.join(appath, "..", "data", "circuits_datastore.json")

    global _store
    _store = CircuitsStore(store_path)

    return _app


def get_store():
    global _store
    return _store


def get_app():
    global _app
    return _app


def get_font_awesome():
    global _font_awesome
    return _font_awesome
