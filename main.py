#.\venv\Scripts\activate
# deactivate
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import sys
from checker import check_tcp 
from console_window import ConsoleWindow


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main_window.ui", self)

        self.console = ConsoleWindow()
        self.openConsoleButton.clicked.connect(self.console.show)

        # buttom
        self.checkButton.clicked.connect(self.run_check)

        # style
        self.setStyleSheet("background-color: black;")  # green window

        # all QLabel and QLineEdit with green 
        widgets = [
            self.findChild(QtWidgets.QLabel, "label"),       # name TCP Checker
            self.findChild(QtWidgets.QLabel, "label_2"),     # Host
            self.findChild(QtWidgets.QLabel, "label_3"),     # Port
            self.findChild(QtWidgets.QLabel, "statusLabel"), # status
            self.findChild(QtWidgets.QLineEdit, "hostInput"),
            self.findChild(QtWidgets.QLineEdit, "portInput")
        ]
        for w in widgets:
            w.setStyleSheet("""
                color: #00FF00;
                background-color: black;
                font-family: 'Courier';
            """)

        # buttom in green style
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
        result = check_tcp(host, port)
        # result in statusLabel
        self.statusLabel.setText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
