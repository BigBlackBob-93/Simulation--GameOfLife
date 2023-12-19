from PyQt6.QtCore import QTimer


class Timer:
    def __init__(self):
        self.time = None

    def start(self, funct):
        self.time: QTimer = QTimer()
        self.time.start()
        self.time.setInterval(100)
        self.time.timeout.connect(funct)

    def stop(self):
        self.time.stop()
        self.time.deleteLater()
