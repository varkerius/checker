import socket

def check_tcp(host, port):
    try:
        port = int(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return f"[OPEN] {host}:{port}"
        else:
            return f"[CLOSED] {host}:{port}"
    except ValueError:
        return "Ошибка: Port должен быть числом"
    except Exception as e:
        return f"Ошибка: {e}"
def check_port(self):
    host = self.hostInput.text()
    port = self.portInput.text()

    self.console.log(f"> Проверка {host}:{port}")

    if check_tcp(host, port):
        self.statusLabel.setText("Открыт ✅")
        self.console.log("> Соединение установлено")
    else:
        self.statusLabel.setText("Закрыт ❌")
        self.console.log("> Соединение не удалось")
