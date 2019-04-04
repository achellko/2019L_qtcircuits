from PyQt5.QtWidgets import QApplication


def tr(s):
    return app.translate("@default",s)


def init(translator):
    global app
    app = QApplication([])
    return app


def get_app():
    global app
    return app
