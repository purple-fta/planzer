import typing
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget


class AbstractMainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__()

    def leftToolBar_addWidget(self, widget: QWidget):
        pass
    
    def rightToolBar_addWidget(self, widget: QWidget):
        pass

    def centerToolBar_addWidget(self, widget: QWidget):
        pass
 
