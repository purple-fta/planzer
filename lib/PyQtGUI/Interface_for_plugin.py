from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget


class InterfaceForPlugin(QMainWindow):
    """
        An interface through which plugins can interact with a window
    """

    # TODO: параметры
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__()

    def add_widget_to_toolbar_left(self, widget: QWidget):
        """
        Adds a widget to the left side of the toolbar

        Args:
            widget:
        """
        pass

    def add_widget_to_toolbar_right(self, widget: QWidget):
        """
        Adds a widget to the right side of the toolbar

        Args:
            widget:
        """
        pass

    def add_widget_to_toolbar_center(self, widget: QWidget):
        """
        Adds a widget to the center side of the toolbar

        Args:
            widget:
        """
        pass
