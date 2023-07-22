import sys
import typing

from PyQt5.QtCore import Qt, QParallelAnimationGroup, QPropertyAnimation, QByteArray, QAbstractAnimation, QRect, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QMainWindow, QToolButton, QSplitter, QDockWidget, QTabBar,
                             QScrollArea, QFrame, QSizePolicy, QLayout, QSpacerItem, QToolBar,  QPushButton, QLineEdit, QMdiArea, QTextEdit)

from lib.PyQtGUI.KWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUI()

        self.setupStyle()

    def setupStyle(self):
        self.setStyleSheet("background-color: #282a36; color: #f8f8f2")

    def setupUI(self):
        # SIDEBAR
        sidebar_widget = QFrame()
        sidebar_widget.setFrameShape(QFrame.Shape.Box)
        sidebar_layout = QVBoxLayout(sidebar_widget)
        sidebar_layout.layout().addWidget(QLabel("PLANZER"))  # logo
        sidebar_layout.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # TOOLBAR
        toolbar_widget = QWidget()
        toolbar_widget.setMaximumHeight(40)
        toolbar_widget.setMinimumHeight(40)
        toolbar_layout = QHBoxLayout(toolbar_widget)
        toolbar_layout.addWidget(QPushButton("1"))
        toolbar_layout.addWidget(QPushButton("2"))
        toolbar_layout.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.create_task_button = QPushButton("+")
        self.create_task_button.clicked.connect(self.showPopupNewTask)
        toolbar_layout.addWidget(self.create_task_button)
        toolbar_layout.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))
        toolbar_layout.addWidget(QPushButton("С"))
        toolbar_layout.addWidget(QPushButton("Т"))
        toolbar_layout.addWidget(QPushButton("К"))
        toolbar_layout.addWidget(QPushButton("Н"))

        # WORKSPACE
        workspace_widget = QSplitter()
        workspace_widget.addWidget(KTaskList())

        # WIDGET WITH TOOLBAR AND WORKSPACE
        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(toolbar_widget) 
        central_layout.addWidget(workspace_widget) 

        # MAIN WIDGET
        main_widget = QSplitter()
        QHBoxLayout(main_widget)
        main_widget.layout().addWidget(sidebar_widget)
        main_widget.layout().addWidget(central_widget)

        self.setCentralWidget(main_widget)
    
    def showPopupNewTask(self):
        popup_widget = KNewTaskPopupWidget(self)
        pos = self.create_task_button.mapTo(self, QtCore.QPoint(0, 0))
        print(pos)
        popup_widget.show(pos.x(), pos.y())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
