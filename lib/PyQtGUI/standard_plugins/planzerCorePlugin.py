from lib.PyQtGUI.AbstractPlugin import *
from lib.PyQtGUI.KWidgets import *


class PlanzerCorePlugin(AbstractPlugin):
    def __init__(self, ui) -> None:
        super().__init__(ui)

        self.create_task_button   = QPushButton("+")
        self.list_tool_button     = QToolButton()
        self.calendar_tool_button = QToolButton()

        self.setupLocalization()
        self.setupUI()
        self.setupConnects()

    def setupLocalization(self):
        self.calendar_tool_button.setText("C")
        self.list_tool_button.setText("L")

    def setupUI(self):
        self.ui.centerToolBar_addWidget(self.create_task_button)
        self.ui.rightToolBar_addWidget(self.list_tool_button)
        self.ui.rightToolBar_addWidget(self.calendar_tool_button)

    def setupConnects(self):
        self.create_task_button.clicked.connect(self._showCreateTaskWindow)
        # TODO: add_widget_to_workspace нет в абстракции
        self.list_tool_button.clicked.connect(lambda: self.ui.add_widget_to_workspace(KTaskList()))
        self.calendar_tool_button.clicked.connect(lambda: self.ui.create_new_window(KCalendar()))

    def _showCreateTaskWindow(self):
        pass

plugin_class = PlanzerCorePlugin
