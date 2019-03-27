from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication


def tr(s):
    return app.translate("@default", s)


def init():
    global app
    app = QApplication([])

    print(QFontDatabase.addApplicationFont("resources/FontAwesome.otf"))

    global fontAwesome
    fontAwesome = QFont()
    fontAwesome.setFamily("Font Awesome 5 Free")

    return app


def get_app():
    global app
    return app

def get_font_awesome():
    global fontAwesome
    return fontAwesome