from lib.PyQtGUI.AbstractPlugin import AbstractPlugin
from lib.PyQtGUI.abstractMainWindow import AbstractMainWindow

from PyQt5.QtWidgets import QToolButton


class TabsPlugin(AbstractPlugin):
    def __init__(self, ui: AbstractMainWindow) -> None:
        super().__init__(ui)

        self.first_tab_button = QToolButton()
        self.second_tab_button = QToolButton()
        
        self.set_localization()
        self.setup_ui()
        
    def set_localization(self):
        self.first_tab_button.setText("1")
        self.second_tab_button.setText("2")

    def setup_ui(self):
        self.ui.leftToolBar_addWidget(self.first_tab_button)
        self.ui.leftToolBar_addWidget(self.second_tab_button)


plugin_class = TabsPlugin
