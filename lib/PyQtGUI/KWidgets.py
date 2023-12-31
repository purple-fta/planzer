from PyQt5.QtCore import QAbstractAnimation, Qt, QParallelAnimationGroup, QPropertyAnimation
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QToolButton, QCalendarWidget, \
                            QScrollArea, QFrame, QSizePolicy, QLayout, QSpacerItem, QLineEdit

from lib.core.task import *


class KCollapsibleBox(QWidget):
    """
        List of widgets that can be collapsed and expanded on click
    """
    def __init__(self, title: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # TODO: Облагородить конструктор
        # TODO: Добавить анимации

        self.arrow_button = QToolButton()
        self.arrow_button.setStyleSheet("QToolButton { border: none; }")
        self.arrow_button.setCheckable(True)
        self.arrow_button.setText(title)
        self.arrow_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.arrow_button.setArrowType(Qt.ArrowType.RightArrow)
        # noinspection PyUnresolvedReferences
        self.arrow_button.pressed.connect(self.on_pressed)

        # self.toggle_animation = QParallelAnimationGroup(self)

        self.content_area = QWidget()
        self.content_area.setMinimumHeight(0)
        self.content_area.setMaximumHeight(0)
        self.content_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        QVBoxLayout(self.content_area)

        self.content_layout = QVBoxLayout(self)
        self.content_layout.setSpacing(0)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.addWidget(self.arrow_button)
        self.content_layout.addWidget(self.content_area)

    def on_pressed(self):
        """
        Method to be executed if the expand button is pressed
        """
        checked = self.arrow_button.isChecked()

        self.arrow_button.setArrowType(Qt.ArrowType.DownArrow if checked else Qt.ArrowType.RightArrow)

        if checked:
            self.content_area.setMaximumHeight(16777215)
        else:
            self.content_area.setMaximumHeight(0)

    def set_content_layout(self, layout: QLayout):
        """
        Sets the widgetized layout for the Collapsible Box

        Args:
            layout: with widgets (vertical recommended)
        """

        # TODO: вполне возможно переопределить стандартный setLayout()

        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)

    def add_new_widget(self, widget: QWidget):
        """
        Adds a widget to the list, automatically updates the animation

        Args:
            widget:
        """
        self.content_area.layout().addWidget(widget)


class KWorkspaceWindowTitleBar(QWidget):
    """
        Title bar widget for workspace windows
    """
    # TODO: может сделать проверку, чтобы в воркспейс
    #       можно было добавить только наследников этого класса
    def __init__(self, title: str, parent: QWidget | None = None,) -> None:
        super().__init__(parent)

        QHBoxLayout(self)

        self.layout().addWidget(QLabel(title))

        self.layout().addItem(QSpacerItem(1, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        self.close_button = QToolButton()
        self.close_button.setText("X")
        self.layout().addWidget(self.close_button)

        self.close_button.clicked.connect(lambda: self.parentWidget().setParent(None))  # TODO: нужно освободить память


class KWorkspaceWindow(QWidget):
    """
        Workspace window template. Has a titlebar
    """
    def __init__(self, title: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        QVBoxLayout(self)

        title_bar = KWorkspaceWindowTitleBar(title)

        self.layout().addWidget(title_bar)

