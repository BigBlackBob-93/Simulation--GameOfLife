import sys

from PyQt6.QtWidgets import QApplication

from project.app.simulation import Simulation

if __name__ == "__main__":
    app = QApplication(sys.argv)
    simulation = Simulation()
    simulation.simulate()

    sys.exit(app.exec())
