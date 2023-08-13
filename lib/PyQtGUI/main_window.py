import sys  # to pass arguments from the command line

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QSplitter, QApplication)

from lib.PyQtGUI.KWidgets import *
from lib.PyQtGUI.Interface_for_plugin import InterfaceForPlugin
from lib.plugins import plugins_classes


class MainWindow(InterfaceForPlugin):
    """
        Qt window to display all elements and use all logic. It launches the program
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # SIDEBAR
        self.sidebar_widget = QWidget()
        self.sidebar_widget.setMinimumWidth(350)
        self.sidebar_widget.setMaximumWidth(350)

        # TOOLBAR
        self.toolbar_widget = QWidget()
        self.toolbar_widget.setMaximumHeight(50)
        self.toolbar_widget.setMinimumHeight(50)

        # TOOLBAR SECTIONS
        self.left_toolbar_widget = QWidget()
        self.central_toolbar_widget = QWidget()
        self.right_toolbar_widget = QWidget()

        # TOOLBAR BUTTONS
        self.settings_tool_button = QToolButton()

        # WORKSPACE
        self.workspace_widget = QSplitter()

        # CENTRAL WIDGET WITH TOOLBAR AND WORKSPACE
        self.central_widget = QWidget()

        # MAIN WIDGET
        self.main_widget = QSplitter()

        self.popup_widget = None

        self.set_layouts()
        self.set_style()
        self.setup_ui()
        self.set_connects()

        self.upload_plugins()

    def set_localization(self):
        """
            Set text in UI
        """

    def set_style(self):
        """
            Set UI style
        """
        self.setStyleSheet("background-color: #282a36; color: #f8f8f2;")

        self.left_toolbar_widget.layout().setContentsMargins(0, 0, 0, 0)
        self.right_toolbar_widget.layout().setContentsMargins(0, 0, 0, 0)
        self.central_toolbar_widget.layout().setContentsMargins(0, 0, 0, 0)

        self.toolbar_widget.layout().setContentsMargins(0, 0, 0, 0)

    def set_layouts(self):
        """
            Set empty layouts to widgets
        """
        # SIDEBAR
        self.sidebar_widget.setLayout(QVBoxLayout())

        # TOOLBAR
        self.toolbar_widget.setLayout(QHBoxLayout())

        # TOOLBAR SECTIONS
        self.left_toolbar_widget.setLayout(QHBoxLayout())
        self.central_toolbar_widget.setLayout(QHBoxLayout())
        self.right_toolbar_widget.setLayout(QHBoxLayout())

        # CENTRAL WIDGET WITH TOOLBAR AND WORKSPACE
        self.central_widget.setLayout(QVBoxLayout())

    def setup_ui(self):
        """
           Arrange all elements in layouts. Must call later set_layouts()
        """

        # SIDEBAR
        # TODO: logo > __init__
        self.sidebar_widget.layout().addWidget(QLabel("PLANZER"))  # logo
        self.sidebar_widget.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # TOOLBAR
        self.toolbar_widget.layout().addWidget(self.left_toolbar_widget)
        self.toolbar_widget.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.toolbar_widget.layout().addWidget(self.central_toolbar_widget)
        self.toolbar_widget.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.toolbar_widget.layout().addWidget(self.right_toolbar_widget)

        # CENTRAL WIDGET WITH TOOLBAR AND WORKSPACE
        self.central_widget.layout().addWidget(self.toolbar_widget)
        self.central_widget.layout().addWidget(self.workspace_widget)

        # MAIN WIDGET
        self.main_widget.addWidget(self.sidebar_widget)
        self.main_widget.addWidget(self.central_widget)

        # SET CENTRAL WIDGET
        self.setCentralWidget(self.main_widget)

    def set_connects(self):
        """
            Set connects to initial window widgets
        """
        pass

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.popup_widget is not None:
            if not self.popup_widget.underMouse():
                self.popup_widget.hide()
        return super().mousePressEvent(a0)

    def add_widget_to_workspace(self, widget: QWidget):
        """
        Args:
            widget: Widget for add to workspace
        """
        # TODO: QWidget -> subclass.KWorkspaceWindow, имя, аргумент, комментарий
        self.workspace_widget.addWidget(widget)

    def upload_plugins(self):
        for plugin in plugins_classes:
            plugin(self)

    def leftToolBar_addWidget(self, widget: QWidget):
        self.left_toolbar_widget.layout().addWidget(widget)

    def rightToolBar_addWidget(self, widget: QWidget):
        self.right_toolbar_widget.layout().addWidget(widget)

    def centerToolBar_addWidget(self, widget: QWidget):
        self.central_toolbar_widget.layout().addWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
