import sys  # to pass arguments from the command line

from PyQt5.QtWidgets import (QSplitter)

from lib.PyQtGUI.KWidgets import *
from lib.PyQtGUI.abstract_main_window import AbstractMainWindow
from lib.PyQtGUI.standard_plugins import plugins_classes


class MainWindow(AbstractMainWindow):
    """
        Qt window to display all elements and use all logic. It launches the program
    """

    # TODO: Либо используем аргументы, либо удаляем. Нахер они тут неиспользуемые нужны?
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__()

        # SIDEBAR
        self.sidebar_widget = QWidget()

        # TOOLBAR
        self.toolbar_widget = QWidget()
        self.toolbar_widget.setMaximumHeight(50)
        self.toolbar_widget.setMinimumHeight(50)

        # TOOLBAR SECTIONS
        self.left_toolbar_widget = QWidget()
        self.central_toolbar_widget = QWidget()
        self.right_toolbar_widget = QWidget()

        # TOOLBAR BUTTONS
        self.first_tab_button = QToolButton()
        self.second_tab_button = QToolButton()
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
        self.first_tab_button.setText("1")
        self.second_tab_button.setText("2")

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
        self.workspace_widget.addWidget(widget)

    def showPopupNewTask(self):
        if self.popup_widget is None:
            self.popup_widget = KNewTaskPopupWidget(self)
        pos = self.create_task_button.mapTo(self, QtCore.QPoint(0, 0))
        self.popup_widget.show(pos.x() + int(self.create_task_button.geometry().width() / 2), pos.y())

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
