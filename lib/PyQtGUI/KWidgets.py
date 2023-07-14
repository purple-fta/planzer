from PyQt5.QtCore import Qt, QParallelAnimationGroup, QPropertyAnimation, QByteArray, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QMainWindow, QToolButton, QScrollArea, QFrame, QSizePolicy, QLayout, QSpacerItem


class KCollapsibleBox(QWidget):
    def __init__(self, title: str, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__()

        self.arrow_button = QToolButton()
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
        
        collapsed_height = self.sizeHint().height() - self.content_area.maximumHeight()
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(250) # type: ignore
            animation.setStartValue(collapsed_height) # type: ignore
            animation.setEndValue(collapsed_height + content_height) # type: ignore
        
        content_animation = self.toggle_animation.animationAt(self.toggle_animation.animationCount() - 1)

        content_animation.setDuration(250) # type: ignore
        content_animation.setStartValue(0) # type: ignore
        content_animation.setEndValue(content_height) # type: ignore
