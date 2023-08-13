from lib.PyQtGUI.AbstractPlugin import AbstractPlugin
from lib.PyQtGUI.Interface_for_plugin import InterfaceForPlugin

from PyQt5.QtWidgets import QToolButton, QSplitter


class TabsPlugin(AbstractPlugin):
    """
        Plugin for tabs with different sets of windows in workspaces
    """
    def __init__(self, ui: InterfaceForPlugin) -> None:
        super().__init__(ui)

        self.first_tab_button = QToolButton()
        self.second_tab_button = QToolButton()

        self.first_tab_splitter_widget = QSplitter()
        self.second_tab_splitter_widget = QSplitter()

        self.setup_connects()
        self.set_localization()
        self.setup_ui()

        # INITIAL STATE
        self.select_first_tab()


    def set_localization(self):
        """
            Set text in UI
        """
        self.first_tab_button.setText("1")
        self.second_tab_button.setText("2")

    def setup_ui(self):
        """
           Arrange all elements in layouts
        """
        self.ui.leftToolBar_addWidget(self.first_tab_button)
        self.ui.leftToolBar_addWidget(self.second_tab_button)

        self.ui.central_widget.layout().removeWidget(self.ui.workspace_widget)
        self.ui.workspace_widget = self.first_tab_splitter_widget
        self.ui.central_widget.layout().addWidget(self.first_tab_splitter_widget)
        self.ui.central_widget.layout().addWidget(self.second_tab_splitter_widget)

    def setup_connects(self):
        self.first_tab_button.clicked.connect(lambda: self.select_first_tab())
        self.second_tab_button.clicked.connect(lambda: self.select_second_tab())

    def select_first_tab(self):
        self.first_tab_button.setDisabled(True)
        self.second_tab_button.setEnabled(True)

        self.ui.workspace_widget = self.first_tab_splitter_widget

        self.first_tab_splitter_widget.show()
        self.second_tab_splitter_widget.hide()

    def select_second_tab(self):
        self.second_tab_button.setDisabled(True)
        self.first_tab_button.setEnabled(True)

        self.ui.workspace_widget = self.second_tab_splitter_widget

        self.first_tab_splitter_widget.hide()
        self.second_tab_splitter_widget.show()


plugin_class = TabsPlugin
