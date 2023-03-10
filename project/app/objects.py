from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QTableWidget,
)
from project import config

# table
table = QTableWidget()
table.setWindowTitle("Simulation: Game of life - RESULTS")
table.setGeometry(0, 0, 1600, 950)
table.setColumnCount(config.MAX_WIDTH)
table.setRowCount(config.MAX_HEIGHT)
for num in range(table.columnCount()):
    table.setColumnWidth(num, 1)

# window
window = QMainWindow()
window.setWindowTitle("Simulation: Game of life")
window.setGeometry(table.width() + 20, 300, 270, 200)


# labels
def set_label(label: QLabel, text: str, above: int, left: int = 20) -> None:
    label.setText(text)
    label.move(left, above)


main_l = QLabel(window)
set_label(main_l, "Choose initial state:", above=10, left=80)


# buttons
def set_btn(btn: QPushButton, label: str, above: int, left: int):
    btn.setText(label)
    btn.move(left, above)
    btn.setFixedWidth(80)


random_btn = QPushButton(window)
set_btn(random_btn, "Random", above=50, left=10)

pulsar_btn = QPushButton(window)
set_btn(pulsar_btn, "Pulsar", above=50, left=90)

gosper_gun_btn = QPushButton(window)
set_btn(gosper_gun_btn, "Gosper gun", above=50, left=170)

launch_btn = QPushButton(window)
set_btn(launch_btn, "Start/Stop", above=140, left=40)

reset_btn = QPushButton(window)
set_btn(reset_btn, "Reset", above=140, left=150)

window.show()
table.show()
