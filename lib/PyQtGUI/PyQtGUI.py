import sys
import typing

from PyQt5.QtCore import Qt, QParallelAnimationGroup, QPropertyAnimation, QByteArray, QAbstractAnimation, QRect, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QMainWindow, QToolButton, QSplitter, QDockWidget, QTabBar,
                             QScrollArea, QFrame, QSizePolicy, QLayout, QSpacerItem, QToolBar,  QPushButton, QLineEdit, QMdiArea, QTextEdit, QStyle)

from lib.PyQtGUI.KWidgets import *

from lib.core.task import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUI()
        self.setupConnects()
        self.setupStyle()

    def setupStyle(self):
        self.setStyleSheet("background-color: #282a36; color: #f8f8f2")

    def setupUI(self):
        # SIDEBAR
        sidebar_widget = QWidget()
        sidebar_layout = QVBoxLayout(sidebar_widget)
        sidebar_layout.layout().addWidget(QLabel("PLANZER"))  # logo
        sidebar_layout.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # TOOLBAR
        toolbar_widget = QWidget()
        toolbar_widget.setMaximumHeight(40)
        toolbar_widget.setMinimumHeight(40)
        toolbar_layout = QHBoxLayout(toolbar_widget)
        self.first_tab_button = QToolButton()
        self.first_tab_button.setText("1")
        self.second_tab_button = QToolButton()
        self.second_tab_button.setText("2")
        toolbar_layout.addWidget(self.first_tab_button)
        toolbar_layout.addWidget(self.second_tab_button)
        toolbar_layout.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.create_task_button = QPushButton("+")
        toolbar_layout.addWidget(self.create_task_button)
        toolbar_layout.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.list_tool_button = QToolButton()
        self.list_tool_button.setText("L")
        toolbar_layout.addWidget(self.list_tool_button)
        self.calendar_tool_button = QToolButton()
        self.calendar_tool_button.setText("C")
        toolbar_layout.addWidget(self.calendar_tool_button)
        self.settings_tool_button = QToolButton()
        self.settings_tool_button.setText("S")
        toolbar_layout.addWidget(self.settings_tool_button)


        # WORKSPACE
        self.workspace_widget = QSplitter()
        task_list = KTaskList()
        task_list.addTask(Task("Lorem", Priority.high, [Tag(" #Tag1 ", QtGui.QColor(255, 184, 108)), Tag(" #Tag2 ", QtGui.QColor(189, 147, 249))], None, datetime(2024, 10, 10)))
        self.workspace_widget.addWidget(task_list)

        # WIDGET WITH TOOLBAR AND WORKSPACE
        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(toolbar_widget) 
        central_layout.addWidget(self.workspace_widget) 

        # MAIN WIDGET
        main_widget = QSplitter()
        QHBoxLayout(main_widget)
        main_widget.layout().addWidget(sidebar_widget)
        main_widget.layout().addWidget(central_widget)

        self.setCentralWidget(main_widget)
    
    def setupConnects(self):
        self.create_task_button.clicked.connect(self.showPopupNewTask)
        self.calendar_tool_button.clicked.connect(lambda: self._create_new_window(KCalendar()))

    def _create_new_window(self, widget):
        self.workspace_widget.addWidget(widget)

    def showPopupNewTask(self):
        popup_widget = KNewTaskPopupWidget(self)
        pos = self.create_task_button.mapTo(self, QtCore.QPoint(0, 0))
        popup_widget.show(pos.x()+int(self.create_task_button.geometry().width()/2), pos.y())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
