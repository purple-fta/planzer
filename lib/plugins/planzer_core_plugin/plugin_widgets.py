from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy, QCalendarWidget, QHBoxLayout, QLabel, QVBoxLayout, \
                            QFrame, QLineEdit, QPushButton

from lib.PyQtGUI.KWidgets import KWorkspaceWindow, KCollapsibleBox
from lib.core import Task, Priority


class CalendarWindow(KWorkspaceWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__("Calendar", parent)

        self.layout().addWidget(QCalendarWidget())


class TaskInList(QWidget):
    """
        A task widget to display in the Task List window.
    """
    def __init__(self, task: Task, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.task = task

        self.setLayout(QVBoxLayout())

        tags_widget = QWidget()
        tags_widget.setLayout(QHBoxLayout())
        for tag in task.tags:
            label = QLabel(tag.name)
            label.setStyleSheet(f"background-color: rgba{tag.decor.getRgb()}; border-radius: 5px")
            tags_widget.layout().addWidget(label)

        tags_widget.layout().addItem(QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        deadline_widget = QWidget()
        deadline_widget.setLayout(QHBoxLayout())
        deadline_widget.layout().addWidget(QLabel("D"))
        deadline_widget.layout().addWidget(QLabel(str(task.deadline)))
        deadline_widget.layout().addItem(QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.layout().addWidget(QLabel(task.name))
        self.layout().addWidget(tags_widget)
        self.layout().addWidget(deadline_widget)


class TaskListWindow(KWorkspaceWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__("Task List", parent)

        self.high_priority_list = KCollapsibleBox("High")
        self.normal_priority_list = KCollapsibleBox("normal")
        self.low_priority_list = KCollapsibleBox("low")

        self.layout().addWidget(self.high_priority_list)
        self.layout().addWidget(self.normal_priority_list)
        self.layout().addWidget(self.low_priority_list)

        self.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def add_task(self, task: Task):
        """
        Adds a new task to the list widget

        Args:
            task:
        """
        task_widget = TaskInList(task)

        if task.priority == Priority.high:
            self.high_priority_list.add_new_widget(task_widget)
        elif task.priority == Priority.normal:
            self.normal_priority_list.add_new_widget(task_widget)
        elif task.priority == Priority.low:
            self.low_priority_list.add_new_widget(task_widget)


class NewTaskPopupWidget(QFrame):
    """
    Popup window for creating a task. Overrides all widgets
    """
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setStyleSheet(
            "QFrame {background: rgba(68, 71, 90, 1); border-radius: 10px;}")  # Установите желаемый стиль виджета
        self.setMinimumWidth(350)
        self.setMinimumHeight(100)

        QHBoxLayout(self)

        self.layout().addWidget(QLabel("POPUP"))
        self.layout().addWidget(QLineEdit())
        self.layout().addWidget(push_button := QPushButton("CREATE"))

        push_button.clicked.connect(self.push_button_clicked)

    def push_button_clicked(self):
        """
        Method called when the create button is clicked
        """
        self.hide()  # TODO: нужно как-то освободить память. Сейчас оно его скрывает, но не удаляет

    def show(self, x: int, y: int) -> None:
        """
        Displays the widget so that the middle of the widget's
        length is at the x, y coordinates and 30 pixels down

        Args:
            x:
            y:
        """
        # TODO: нужно ли переопределять метод?
        self.move(int(x - self.geometry().width() / 2), y + 30)
        super().show()

