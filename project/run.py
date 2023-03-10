if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    from project.app import objects
    from project.app import signals

    sys.exit(app.exec())