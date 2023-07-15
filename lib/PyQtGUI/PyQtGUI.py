import sys
import typing

from PyQt5.QtCore import Qt, QParallelAnimationGroup, QPropertyAnimation, QByteArray, QAbstractAnimation
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QMainWindow, QToolButton, 
                             QScrollArea, QFrame, QSizePolicy, QLayout, QSpacerItem, QToolBar,  QPushButton, QLineEdit, QMdiArea)

from KWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        sidebar_widget = QWidget()
        sidebar_widget.setMaximumWidth(250)
        self.setStyleSheet("border-color: black; border-width: 2px; border-style: outset; border-radius: 5px")
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


        toolbar_widget = QWidget()
        toolbar_layout = QHBoxLayout(toolbar_widget)
        toolbar_layout.addWidget(QPushButton("Вкладка 1"))
        toolbar_layout.addWidget(QPushButton("Вкладка 2"))
        toolbar_layout.addWidget(QPushButton(" + "))
        toolbar_layout.addWidget(QLineEdit())
        toolbar_layout.addWidget(QPushButton("Список"))
        toolbar_layout.addWidget(QPushButton("ТаймЛайн"))
        toolbar_layout.addWidget(QPushButton("Календарь"))
        toolbar_layout.addWidget(QPushButton("НАСТРОЙКИ"))

        mdi_area_widget = QMdiArea()

        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(toolbar_widget)
        central_layout.addWidget(mdi_area_widget)
       

        main_widget = QWidget()
        QHBoxLayout(main_widget)
        main_widget.layout().addWidget(sidebar_widget)
        main_widget.layout().addWidget(central_widget)


        self.setCentralWidget(main_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
