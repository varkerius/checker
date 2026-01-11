from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QFileDialog
from PyQt6.QtCore import QDateTime

class ConsoleWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/console_window.ui", self)
        self.setWindowTitle("TCP Checker — Console")

        self.logs = []

        # кнопки и фильтр
        self.clearButton.clicked.connect(self.clear_logs)
        self.exportButton.clicked.connect(self.export_logs)
        self.filterCombo.currentTextChanged.connect(self.apply_filter)

    def log(self, level: str, message: str):
        timestamp = QDateTime.currentDateTime().toString("HH:mm:ss")
        entry = f"[{timestamp}] [{level}] {message}"
        self.logs.append((level, entry))
        # вывод в консоль
        if self.filterCombo.currentText() in ("ALL", level):
            self.consoleOutput.appendPlainText(entry)

    def clear_logs(self):
        self.consoleOutput.clear()
        self.logs.clear()

    def export_logs(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Export logs", "logs.txt", "Text Files (*.txt)"
        )
        if path:
            with open(path, "w", encoding="utf-8") as f:
                for _, entry in self.logs:
                    f.write(entry + "\n")

    def apply_filter(self, level):
        self.consoleOutput.clear()
        for log_level, entry in self.logs:
            if level == "ALL" or level == log_level:
                self.consoleOutput.appendPlainText(entry)
