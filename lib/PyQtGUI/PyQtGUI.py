import sys
import typing

from PyQt5.QtCore import Qt, QParallelAnimationGroup, QPropertyAnimation, QByteArray, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QMainWindow, QToolButton, QScrollArea, QFrame, QSizePolicy, QLayout, QSpacerItem

from KWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        sidebar_widget = QWidget()
        QVBoxLayout(sidebar_widget)
        logo = QLabel("PLANZER")
        sidebar_widget.layout().addWidget(logo)
        cb = KCollapsibleBox("11111111")
        l = QVBoxLayout()
        l.addWidget(QLabel("123"))
        l.addWidget(QLabel("123"))
        l.addWidget(QLabel("123"))
        l.addWidget(QLabel("123"))
        l.addWidget(QLabel("123"))
        cb.setContentLayout(l)
        sidebar_widget.layout().addWidget(cb)
        sidebar_widget.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


        central_widget = QWidget()
        QHBoxLayout(central_widget)
        central_widget.layout().addWidget(sidebar_widget)


        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
