from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

class ConsoleWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/console_window.ui", self)
        self.setWindowTitle("TCP Checker — Console")

        self.clearButton.clicked.connect(self.consoleOutput.clear)

    def log(self, message: str):
        self.consoleOutput.appendPlainText(message)
