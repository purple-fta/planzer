from PyQt5 import QtCore
from PyQt5.QtWidgets import QToolButton

from lib.PyQtGUI.AbstractPlugin import *
from lib.plugins.planzer_core_plugin.plugin_widgets import *


class PlanzerCorePlugin(AbstractPlugin):
    """
        The main plugin for creating tasks, scheduling, etc.
    """
    def __init__(self, ui) -> None:
        super().__init__(ui)

        self.create_task_button = QPushButton("+")
        self.list_tool_button  = QToolButton()
        self.calendar_tool_button = QToolButton()

        self.popup_widget_create_task = None

        self.setup_localization()
        self.setup_ui()
        self.setup_connects()

    def setup_localization(self):
        """
            Set text in UI
        """
        self.calendar_tool_button.setText("C")
        self.list_tool_button.setText("L")

    def setup_ui(self):
        """
           Arrange all elements in layouts
        """
        self.ui.centerToolBar_addWidget(self.create_task_button)
        self.ui.rightToolBar_addWidget(self.list_tool_button)
        self.ui.rightToolBar_addWidget(self.calendar_tool_button)

    def setup_connects(self):
        """
            Set connects to widgets
        """
        self.create_task_button.clicked.connect(self._show_create_task_window)
        self.list_tool_button.clicked.connect(lambda: self.ui.add_widget_to_workspace(TaskListWindow()))
        self.calendar_tool_button.clicked.connect(lambda: self.ui.add_widget_to_workspace(CalendarWindow()))

    def _show_create_task_window(self):
        if self.popup_widget_create_task is None:
            self.popup_widget_create_task = NewTaskPopupWidget(self.ui)
        pos = self.create_task_button.mapTo(self.ui, QtCore.QPoint(0, 0))
        self.popup_widget_create_task.show(pos.x() + int(self.create_task_button.geometry().width() / 2), pos.y())


plugin_class = PlanzerCorePlugin
