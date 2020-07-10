import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import PyQt5.uic as uic
import os


class MW(QMainWindow):
    def __init__(self, tabs):
        super(MW, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "forms/main_window.ui"), self)

        self.tabWidget.removeTab(0)
        self.tabWidget.removeTab(0)

        for tab in tabs:
            self.tabWidget.addTab(tab, tab.name)


class Backend:
    def fun1(self):
        print("fun1")

    def fun2(self):
        print("fun2")


class Backend2:
    def fun3(self):
        print("fun3")

    def fun4(self):
        print("fun4")


class SomeTab(QWidget):
    def __init__(self, backend, name):
        super(SomeTab, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "forms/proces_abc.ui"), self)
        self.backend = backend
        self.but1.clicked.connect(self.backend.fun1)
        self.but2.clicked.connect(self.backend.fun2)
        self.name = name


class SomeOtherTab(QWidget):
    def __init__(self, backend, name):
        super(SomeOtherTab, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "forms/proces_def.ui"), self)
        self.backend = backend
        self.but1.clicked.connect(self.backend.fun3)
        self.but2.clicked.connect(self.backend.fun4)
        self.name = name


def prepare_tabs():
    return [SomeTab(Backend(), "Dynamic entry"), SomeOtherTab(Backend2(), "Another one")]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.processEvents()

    tabs = prepare_tabs()
    gui = MW(tabs)

    gui.show()

    sys.exit(app.exec_())
