#.\venv\Scripts\activate
# deactivate
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import sys
import time
from checker import check_tcp
from console_window import ConsoleWindow

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main_window.ui", self)

        # new console
        self.console = ConsoleWindow()
        self.openConsoleButton.clicked.connect(self.console.show)

        # check button
        self.checkButton.clicked.connect(self.run_check)

        # windows and widgets
        self.setStyleSheet("background-color: black;")

        widgets = [
            self.findChild(QtWidgets.QLabel, "label"),
            self.findChild(QtWidgets.QLabel, "label_2"),
            self.findChild(QtWidgets.QLabel, "label_3"),
            self.findChild(QtWidgets.QLabel, "statusLabel"),
            self.findChild(QtWidgets.QLineEdit, "hostInput"),
            self.findChild(QtWidgets.QLineEdit, "portInput")
        ]
        for w in widgets:
            w.setStyleSheet("""
                color: #00FF00;
                background-color: black;
                font-family: 'Courier';
            """)

        # green buttons
        self.checkButton.setStyleSheet("""
            color: black;
            background-color: #00FF00;
            font-family: 'Courier';
        """)
        self.openConsoleButton.setStyleSheet("""
            color: black;
            background-color: #00FF00;
            font-family: 'Courier';
        """)

    def run_check(self):
        host = self.hostInput.text()
        port = self.portInput.text()

        if not host or not port:
            self.statusLabel.setText("Enter host and port")
            self.console.log("ERROR", "Empty fields")
            return

        start = time.perf_counter()
        self.console.log("INFO", f"Checking {host}:{port}")

        result = check_tcp(host, port)
        elapsed = (time.perf_counter() - start) * 1000

        if result is None:
            self.statusLabel.setText("Error ❌")
            self.console.log("ERROR", "Port must be a number")
        elif result:
            self.statusLabel.setText("Open ✅")
            self.console.log("SUCCESS", f"Connection established {elapsed:.1f} ms")
        else:
            self.statusLabel.setText("Closed ❌")
            self.console.log("ERROR", f"Connection failed in {elapsed:.1f} ms")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
