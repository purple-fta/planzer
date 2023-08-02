from lib.PyQtGUI.abstractMainWindow import AbstractMainWindow

class AbstractPlugin:
    def __init__(self, ui: AbstractMainWindow, name: str, description: str) -> None:
        self.ui = ui
        self.name = name
        self.description = description
