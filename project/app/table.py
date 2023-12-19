from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
)

from project import constants


class Table:
    def __init__(self):
        self.table: QTableWidget = QTableWidget()
        self.set_table()

    def set_table(self):
        self.table.setWindowTitle("Simulation: Game of life - RESULTS")
        self.table.setGeometry(0, 0, constants.TABLE_WIDTH, constants.TABLE_HEIGHT)
        self.table.setColumnCount(constants.COLUMN_WIDTH)
        self.table.setRowCount(constants.ROW_HEIGHT)
        for num in range(self.table.columnCount()):
            self.table.setColumnWidth(num, 1)

    def set_item(self, position: tuple):
        self.table.setItem(
            position[1],
            position[0],
            QTableWidgetItem(' '),
        )

    def set_color(self, position: tuple, color: str = constants.ALIVE_COL):
        self.table.item(
            position[1],
            position[0],
        ).setBackground(
            QtGui.QColor(color)
        )
