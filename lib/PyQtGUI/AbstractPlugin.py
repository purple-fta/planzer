from lib.PyQtGUI.abstract_main_window import AbstractMainWindow


class AbstractPlugin:
    def __init__(self, ui: AbstractMainWindow) -> None:
        self.ui = ui
        self.name = "Name"
        self.description = "Description"
