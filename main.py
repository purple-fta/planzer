from PyQt5 import QtWidgets
from lib.PyQtGUI.main_window import MainWindow

app = QtWidgets.QApplication([])
window = MainWindow()
window.show()

app.exec()
