import datetime

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QToolButton

from lib.PyQtGUI.AbstractPlugin import *
from lib.core import Tag, PlanzerCore
from lib.plugins.planzer_core_plugin.plugin_widgets import *


core = PlanzerCore()


class PlanzerCorePlugin(AbstractPlugin):
    """
        The main plugin for creating tasks, scheduling, etc.
    """
    def __init__(self, ui) -> None:
        super().__init__(ui)

        self.core = core

        self.create_task_button = QPushButton("+")
        self.list_tool_button  = QToolButton()
        self.events_tool_button  = QToolButton()
        self.calendar_tool_button = QToolButton()

        # TODO: SINGLETON?
        self.task_list_window = TaskListWindow()
        self.event_window = EventsWindow()

        self.task_list_window.connect_core(core)

        self.text_for_priority_combobox = {"High": Priority.high, "Normal": Priority.normal, "Low": Priority.low}
        self.popup_widget_create_task = NewTaskPopupWidget(self.text_for_priority_combobox, self.ui)
        self.popup_widget_create_task.hide()

        self.setup_localization()
        self.setup_ui()
        self.setup_connects()

    def setup_localization(self):
        """
            Set text in UI
        """
        self.calendar_tool_button.setText("C")
        self.events_tool_button.setText("E")
        self.list_tool_button.setText("L")

    def setup_ui(self):
        """
           Arrange all elements in layouts
        """
        self.ui.centerToolBar_addWidget(self.create_task_button)
        self.ui.rightToolBar_addWidget(self.list_tool_button)
        self.ui.rightToolBar_addWidget(self.events_tool_button)
        self.ui.rightToolBar_addWidget(self.calendar_tool_button)

    def setup_connects(self):
        """
            Set connects to widgets
        """
        self.create_task_button.clicked.connect(self._show_create_task_window)
        self.list_tool_button.clicked.connect(lambda: self.ui.add_widget_to_workspace(self.task_list_window))
        self.events_tool_button.clicked.connect(lambda: self.ui.add_widget_to_workspace(self.event_window))
        self.calendar_tool_button.clicked.connect(lambda: self.ui.add_widget_to_workspace(CalendarWindow()))

        self.popup_widget_create_task.create_push_button.clicked.connect(lambda: self._create_task())

    def _create_task(self):
        name = self.popup_widget_create_task.name_input.text()
        priority = self.text_for_priority_combobox[self.popup_widget_create_task.priority_combobox.currentText()]
        tags = self.popup_widget_create_task.add_tags_widget.tags
        task = Task(name, priority, tags, None, datetime.datetime.now())

        self.core.add_task(task)
        self.task_list_window.add_task(task)
        self.task_list_window.high_priority_list.update()

        self.popup_widget_create_task.reset_input_data()

    def _show_create_task_window(self):
        pos = self.create_task_button.mapTo(self.ui, QtCore.QPoint(0, 0))
        self.popup_widget_create_task.show(pos.x() + int(self.create_task_button.geometry().width() / 2), pos.y())


plugin_class = PlanzerCorePlugin
