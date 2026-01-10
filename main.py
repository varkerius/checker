#.\venv\Scripts\activate
# deactivate
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import sys
from checker import check_tcp  # твоя логика проверки TCP
from console_window import ConsoleWindow


class MainWindow(QtWidgets.QWidget):  # или QMainWindow
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main_window.ui", self)

        self.console = ConsoleWindow()
        self.openConsoleButton.clicked.connect(self.console.show)

        # Кнопка
        self.checkButton.clicked.connect(self.run_check)

        # Стили "старого терминала"
        self.setStyleSheet("background-color: black;")  # фон всего окна

        # Все QLabel и QLineEdit зелёные с моноширинным шрифтом
        widgets = [
            self.findChild(QtWidgets.QLabel, "label"),       # Заголовок TCP Checker
            self.findChild(QtWidgets.QLabel, "label_2"),     # Host
            self.findChild(QtWidgets.QLabel, "label_3"),     # Port
            self.findChild(QtWidgets.QLabel, "statusLabel"), # Статус
            self.findChild(QtWidgets.QLineEdit, "hostInput"),
            self.findChild(QtWidgets.QLineEdit, "portInput")
        ]
        for w in widgets:
            w.setStyleSheet("""
                color: #00FF00;
                background-color: black;
                font-family: 'Courier';
            """)

        # Кнопка в зелёном стиле
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
        # Выводим результат в статусLabel
        self.statusLabel.setText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
