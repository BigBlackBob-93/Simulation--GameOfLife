from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
)
from project import constants


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Simulation: Game of life")
        self.setGeometry(constants.TABLE_WIDTH + 20, 300, 270, 200)

        self.set_label(
            text="Choose initial state:",
            above=10,
            left=80,
        )

        self.btns: list[QPushButton] | None = None

        self.set_btn(label="Random", above=50, left=10)
        self.set_btn(label="Pulsar", above=50, left=90)
        self.set_btn(label="Gosper gun", above=50, left=170)
        self.set_btn(label="Reset", above=140, left=150)
        self.set_btn(label="Start/Stop", above=140, left=40)

    def set_label(self, text: str, above: int, left: int = 20) -> None:
        label: QLabel = QLabel(self)
        label.setText(text)
        label.move(left, above)

    def set_btn(self, label: str, above: int, left: int) -> None:
        btn = QPushButton(self)
        if self.btns is None:
            self.btns = [btn]
        else:
            self.btns.append(btn)
        btn.setText(label)
        btn.move(left, above)
        btn.setFixedWidth(80)

    def set_disable_btn(self, disable: bool) -> None:
        for btn in self.btns[:4]:
            btn.setDisabled(disable)

    def set_btn_click(self, btn_index: int, function) -> None:
        self.btns[btn_index].clicked.connect(function)
