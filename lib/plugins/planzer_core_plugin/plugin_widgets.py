import datetime
from enum import Enum

from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QBrush
from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy, QCalendarWidget, QHBoxLayout, QLabel, QVBoxLayout, \
    QFrame, QLineEdit, QPushButton, QCheckBox, QComboBox, QToolButton, QDateTimeEdit, QTimeEdit, QDateEdit, QRadioButton

from lib.PyQtGUI.KWidgets import KWorkspaceWindow, KCollapsibleBox
from lib.core import Task, Priority, Tag, Timeline, Event, StartEnd, EventOptions

from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal, QLine, QDateTime, QTime
from PyQt5.QtGui import QPainter, QFont, QColor, QPen


class RecalculatedTime(Enum):
    start = 0
    duration = 1
    end = 2


class CalendarWindow(KWorkspaceWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__("Calendar", parent)

        self.layout().addWidget(QCalendarWidget())


class TagWidget(QLabel):
    def __init__(self, tag: Tag, parent: QWidget | None = None):
        super().__init__(f" #{tag.name} ", parent)
        self.setStyleSheet(f"background-color: rgba{tag.decor.getRgb()}; border-radius: 5px")
        self.setMaximumHeight(20)
        self.setMinimumHeight(20)


class TaskInList(QWidget):
    """
        A task widget to display in the Task List window.
    """

    def __init__(self, task: Task, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.task = task

        self.create_event_button = QToolButton()
        self.delete_button = QToolButton()
        self.create_event_button.setText("E")
        self.delete_button.setText("D")

        self.create_event_window = CreateEventPopupWidget()

        QHBoxLayout(self)

        checkbox_layout = QVBoxLayout()
        without_checkbox_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        down_layout = QHBoxLayout()

        checkbox_layout.addWidget(QCheckBox())
        top_layout.addWidget(QLabel(task.name))
        top_layout.addItem(QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        top_layout.addWidget(self.create_event_button)

        for tag in task.tags:
            tag_widget = TagWidget(tag)
            down_layout.addWidget(tag_widget)

        down_layout.addItem(QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        down_layout.addWidget(self.delete_button)

        without_checkbox_layout.addLayout(top_layout)
        without_checkbox_layout.addLayout(down_layout)

        self.layout().addLayout(checkbox_layout)
        self.layout().addLayout(without_checkbox_layout)

        self.create_event_button.clicked.connect(self._show_create_event_window)
        self.create_event_window.create_button.clicked.connect(self._create_event)

    def _create_event(self):
        task = self.task
        options = self.create_event_window.event_options
        event = Event(task, StartEnd(options.event_start_time, options.event_end_time))

    def _show_create_event_window(self):
        self.layout().addWidget(self.create_event_window)


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


class TagInputWidget(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.tags = []

        self.layout = QHBoxLayout()

        self.input = QLineEdit()

        self.layout.addWidget(self.input)

        self.setLayout(self.layout)

        self.input.returnPressed.connect(self.add_tag)

    def add_tag(self):
        new_tag = Tag(self.input.text(), QColor(189, 147, 249))
        self.layout.insertWidget(self.layout.count() - 1, TagWidget(new_tag))
        self.input.setText("")
        self.tags.append(new_tag)


class NewTaskPopupWidget(QFrame):
    """
    Popup window for creating a task. Overrides all widgets
    """

    def __init__(self, text_for_priority_combobox: dict[str, Priority], parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # TODO: выделить всё кроме инициализации полей в отдельные методы

        self.name_input = QLineEdit()
        self.priority_combobox = QComboBox()
        self.add_tags_widget = TagInputWidget()
        self.create_push_button = QPushButton("CREATE")

        self.setStyleSheet(
            "QFrame {background: rgba(68, 71, 90, 1); border-radius: 10px;}")  # Установите желаемый стиль виджета
        self.setMinimumWidth(750)
        self.setMinimumHeight(100)

        QHBoxLayout(self)

        self.layout().addWidget(QLabel("POPUP"))
        self.layout().addWidget(self.name_input)
        self.layout().addWidget(self.priority_combobox)
        self.layout().addWidget(self.add_tags_widget)
        self.layout().addWidget(self.create_push_button)

        self.create_push_button.clicked.connect(self.push_button_clicked)
        self.text_priority = text_for_priority_combobox
        self.add_items_to_priority_combobox()

    def add_items_to_priority_combobox(self):
        for text in self.text_priority:
            self.priority_combobox.addItem(text)

    def push_button_clicked(self):
        """
        Method called when the create button is clicked
        """
        self.hide()  # TODO: нужно как-то освободить память. Сейчас оно его скрывает, но не удаляет

    def reset_input_data(self):
        self.name_input.setText("")

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


class TimelineWidget(QWidget):
    def __init__(self, timeline: Timeline):
        super().__init__()

        self.timeline = timeline

        self.setMinimumSize(130, 90)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_widget(qp)
        qp.end()

    def draw_widget(self, painter):
        width = self.width()
        height = self.height()

        font = QFont('Serif', 12, QFont.Normal)
        painter.setFont(font)
        font_metrics = painter.fontMetrics()

        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(248, 248, 242))

        # BORDER
        painter.drawRoundedRect(0, 0, width, height, 13, 13)
        painter.setBrush(QColor(40, 42, 54))
        painter.drawRoundedRect(2, 2, width - 4, height - 4, 11, 11)

        hour_height_scale = int(height / 24)
        minute_height_scale = hour_height_scale / 60

        # SCALE
        for i in range(1, 24):
            painter.drawLine(QLine(0, i * hour_height_scale, width, i * hour_height_scale))

        # TEXT
        # for i in range(1, 24):
        #    font_width = font_metrics.width(f"{i:0{2}}:00")
        #    painter.drawText(int(width/2-font_width/2), i * hour_height_scale-4, f"{i:0{2}}:00")

        # EVENTS
        for event in self.timeline.events:
            start = event.event_start_time.time().hour * hour_height_scale \
                    + int(event.event_start_time.time().minute * minute_height_scale)
            end = event.event_end_time.time().hour * hour_height_scale \
                + int(event.event_end_time.time().minute * minute_height_scale)
            painter.setBrush(event.task.decor)
            painter.drawRect(2, start, width-4, end)

            # TODO: Нужно как-то выделить те что с высоким приоритетом
            if event.task.priority == Priority.high:
                pass


# TODO: Он уже не POPUP
class CreateEventPopupWidget(QFrame):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        # TODO: Добавим _widget или _button для ясности
        self.date_edit = QDateEdit()

        self.start_time = QTimeEdit()
        self.duration_time = QTimeEdit()
        self.end_time = QTimeEdit()

        self.start_recalculated_radiobutton = QRadioButton()
        self.duration_recalculated_radiobutton = QRadioButton()
        self.end_recalculated_radiobutton = QRadioButton()
        self.end_recalculated_radiobutton.toggle()

        self.create_button = QPushButton("CREATE")

        self.event_options = EventOptions(StartEnd(self.start_time.dateTime().toPyDateTime(),
                                                   self.end_time.dateTime().toPyDateTime()))

        self.recalculated_time = None  # TODO: Нужно указать что оно не блокируется полностью
        # пользователь может изменять, но просчитываться после изменения остальных оно не будет
        self._set_recalculated_time(RecalculatedTime.end)

        self.setStyleSheet(
            "QFrame {background: rgba(68, 71, 90, 1); border-radius: 10px;}")  # Установите желаемый стиль виджета

        QHBoxLayout(self)

        self.layout().addWidget(self.date_edit)
        self.layout().addWidget(self.start_time)
        self.layout().addWidget(self.start_recalculated_radiobutton)
        self.layout().addWidget(self.duration_time)
        self.layout().addWidget(self.duration_recalculated_radiobutton)
        self.layout().addWidget(self.end_time)
        self.layout().addWidget(self.end_recalculated_radiobutton)
        self.layout().addWidget(self.create_button)

        self.create_button.clicked.connect(self.push_button_clicked)

        self.start_time.dateTimeChanged.connect(self._start_time_changed)
        self.duration_time.dateTimeChanged.connect(self._duration_time_changed)
        self.end_time.dateTimeChanged.connect(self._end_time_changed)

        self.start_recalculated_radiobutton.toggled.connect(lambda: self._set_recalculated_time(RecalculatedTime.start))
        self.duration_recalculated_radiobutton.toggled.connect(lambda: self._set_recalculated_time(RecalculatedTime.duration))
        self.end_recalculated_radiobutton.toggled.connect(lambda: self._set_recalculated_time(RecalculatedTime.end))

    def _is_recalculated(self, recalculated_time: RecalculatedTime, value_else_recalculated):
        return None if self.recalculated_time == recalculated_time else value_else_recalculated

    def _set_date(self, added_date: datetime.datetime, time):
        time = datetime.datetime(added_date.year, added_date.month, added_date.day, time.hour, time.minute)

        return time

    @staticmethod
    def _duration_to_timedelta(duration: datetime.datetime) -> datetime.timedelta:
        return datetime.timedelta(hours=duration.hour, minutes=duration.minute)

    def _set_recalculated_time(self, new_recalculated_time: RecalculatedTime):
        # TODO: давай через словарь
        self.start_time.setEnabled(True)
        self.duration_time.setEnabled(True)
        self.end_time.setEnabled(True)

        if new_recalculated_time == RecalculatedTime.start:
            self.start_time.setDisabled(True)
        elif new_recalculated_time == RecalculatedTime.duration:
            self.duration_time.setDisabled(True)
        elif new_recalculated_time == RecalculatedTime.end:
            self.end_time.setDisabled(True)

        self.recalculated_time = new_recalculated_time

    def _timedelta_to_time(self, td: datetime.timedelta) -> datetime.time:
        hour = td.seconds // 3600
        minute = (td.seconds % 3600) // 60

        return datetime.time(hour, minute)

    def _update_time_edits(self):
        self.start_time.setDateTime(self.event_options.event_start_time)
        duration = self._timedelta_to_time(self.event_options.event_duration_time)
        self.duration_time.setTime(duration)
        self.end_time.setDateTime(self.event_options.event_end_time)

    def _start_time_changed(self, new_date: QDateTime):
        new_date = new_date.toPyDateTime()

        date = self.date_edit.date().toPyDate()

        start = new_date
        duration = self._is_recalculated(RecalculatedTime.duration, self.duration_time.dateTime().toPyDateTime())
        end = self._is_recalculated(RecalculatedTime.end, self.end_time.dateTime().toPyDateTime())

        start = None if start is None else self._set_date(date, start)
        end = None if end is None else self._set_date(date, end)
        duration = self._duration_to_timedelta(duration) if duration is not None else None

        self.event_options.set_options(start, duration, end)

        self._update_time_edits()

    def _duration_time_changed(self, new_date: QDateTime):
        new_date = new_date.toPyDateTime()

        date = self.date_edit.date().toPyDate()

        start = self._is_recalculated(RecalculatedTime.start, self.start_time.dateTime().toPyDateTime())
        duration = new_date
        end = self._is_recalculated(RecalculatedTime.end, self.end_time.dateTime().toPyDateTime())

        start = None if start is None else self._set_date(date, start)
        end = None if end is None else self._set_date(date, end)
        duration = self._duration_to_timedelta(duration)

        self.event_options.set_options(start, duration, end)

        self._update_time_edits()

    def _end_time_changed(self, new_date: QDateTime):
        new_date = new_date.toPyDateTime()

        date = self.date_edit.date().toPyDate()

        start = self._is_recalculated(RecalculatedTime.start, self.start_time.dateTime().toPyDateTime())
        duration = self._is_recalculated(RecalculatedTime.duration, self.duration_time.dateTime().toPyDateTime())
        end = new_date

        start = None if start is None else self._set_date(date, start)
        end = None if end is None else self._set_date(date, end)
        duration = self._duration_to_timedelta(duration) if duration is not None else None

        self.event_options.set_options(start, duration, end)

        self._update_time_edits()

    def push_button_clicked(self):
        self.setParent(None)  # TODO: memory?


class EventsWindow(KWorkspaceWindow):
    def __init__(self, parent: QWidget | None = None):
        super().__init__("Events", parent)

        self.widget = None

        self.top_bar_layout = QHBoxLayout()
        self.timelines_layout = QHBoxLayout()

        for i in range(5):
            self.top_bar_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum))
            self.top_bar_layout.addWidget(QPushButton(f"0{i}.10"))
            self.top_bar_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum))

        for i in range(5):
            self.timelines_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum))
            self.timelines_layout.addWidget(TimelineWidget(Timeline({Event(
                Task("Task",
                     Priority.high,
                     [],
                     QColor(255, 121, 198),
                     datetime.datetime(2025, 5,
                                       5, 5)),
                StartEnd(
                    datetime.datetime(2023, 10, 5, 5),
                    datetime.datetime(2023, 10, 5, 12)))},
                datetime.time(),
                datetime.time(23))))
            self.timelines_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum))

        self.layout().addLayout(self.top_bar_layout)
        self.layout().addLayout(self.timelines_layout)
