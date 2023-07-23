import typing
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QSize, QRect, QParallelAnimationGroup, QPropertyAnimation, QByteArray, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QMainWindow, QToolButton, QCalendarWidget, QScrollArea, QFrame, QSizePolicy, QLayout, QSpacerItem, QLineEdit
from lib.core.task import *

class KCollapsibleBox(QWidget):
    def __init__(self, title: str, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__()
        
        self.arrow_button = QToolButton()
        self.arrow_button.setStyleSheet("QToolButton { border: none; }")
        self.arrow_button.setCheckable(True)
        self.arrow_button.setText(title)
        self.arrow_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.arrow_button.setArrowType(Qt.ArrowType.RightArrow)
        self.arrow_button.pressed.connect(self.on_pressed)

        self.toggle_animation = QParallelAnimationGroup(self)

        self.content_area = QScrollArea()
        self.content_area.setMinimumHeight(0)
        self.content_area.setMaximumHeight(0)
        self.content_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.content_area.setFrameStyle(QFrame.Shape.NoFrame)
        QVBoxLayout(self.content_area)
        
        self.content_layout = QVBoxLayout(self)
        self.content_layout.setSpacing(0)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.addWidget(self.arrow_button)
        self.content_layout.addWidget(self.content_area)

        self.toggle_animation.addAnimation(QPropertyAnimation(self, b"minimumHeight")) # type: ignore
        self.toggle_animation.addAnimation(QPropertyAnimation(self, b"maximumHeight")) # type: ignore
        self.toggle_animation.addAnimation(QPropertyAnimation(self.content_area, b"maximumHeight")) # type: ignore

    def on_pressed(self):
        checked = self.arrow_button.isChecked()

        self.arrow_button.setArrowType( Qt.ArrowType.DownArrow if not checked else Qt.ArrowType.RightArrow )

        self.toggle_animation.setDirection( QAbstractAnimation.Direction.Forward if not checked else QAbstractAnimation.Direction.Backward )
        self.toggle_animation.start()

    def setContentLayout(self, layout: QLayout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        
        self.updateContentAnimation()

    def updateContentAnimation(self):
        collapsed_height = self.sizeHint().height() - self.content_area.maximumHeight()
        content_height = self.content_area.layout().sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(250) # type: ignore
            animation.setStartValue(collapsed_height) # type: ignore
            animation.setEndValue(collapsed_height + content_height) # type: ignore
        
        content_animation = self.toggle_animation.animationAt(self.toggle_animation.animationCount() - 1)

        content_animation.setDuration(250) # type: ignore
        content_animation.setStartValue(0) # type: ignore
        content_animation.setEndValue(content_height) # type: ignore

    def addNewWidget(self, widget: QWidget):
        self.content_area.layout().addWidget(widget)
        self.updateContentAnimation()


class KTaskList(QWidget):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__()

        QVBoxLayout(self)

        self.high_priority_list = KCollapsibleBox("High", self)
        self.normal_priority_list = KCollapsibleBox("normal", self)
        self.low_priority_list = KCollapsibleBox("low", self)

        self.layout().addWidget(self.high_priority_list)
        self.layout().addWidget(self.normal_priority_list)
        self.layout().addWidget(self.low_priority_list)

        self.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
    
    def addTask(self, task: Task):
        task_widget = KTaskInList(task)

        if task.priority == Priority.high:
            self.high_priority_list.addNewWidget(task_widget)
        elif task.priority == Priority.normal:
            self.normal_priority_list.addNewWidget(task_widget)
        elif task.priority == Priority.low:
            self.low_priority_list.addNewWidget(task_widget)


class KTaskInList(QWidget):
    def __init__(self, task: Task, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__()

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

class KNewTaskPopupWidget(QWidget):
    def __init__(self, parent: QWidget | None = None, flags: Qt.WindowType = ...) -> None:
        super().__init__(parent)

        self.setStyleSheet("background-color: rgba(248, 248, 0, 1);")  # Установите желаемый стиль виджета
        self.setMinimumWidth(250)
        self.setMinimumHeight(250)
        
        QHBoxLayout(self)

        self.layout().addWidget(QLabel("POPUP"))
        self.layout().addWidget(QLineEdit())
        self.layout().addWidget(push_button := QPushButton("CREATE"))

        push_button.clicked.connect(self.push_button_clicked)

    def push_button_clicked(self):
        self.hide()  #TODO: нужно как-то освободить память. Сейчас оно его скрывает, но не удаляет

    def show(self, x: int, y: int) -> None:
        self.move(x-50, y+50)
        super().show()


class KCalendar(QCalendarWidget):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__()
