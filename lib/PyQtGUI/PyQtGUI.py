from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)


app = QApplication([])

window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()
