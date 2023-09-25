from lib.PyQtGUI.Interface_for_plugin import InterfaceForPlugin


class AbstractPlugin:
    def __init__(self, ui: InterfaceForPlugin) -> None:
        self.ui = ui
        self.name = "Name"
        self.description = "Description"
