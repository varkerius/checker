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
        return "Error: Port must be a number"
    except Exception as e:
        return f"Error: {e}"
def check_port(self):
    host = self.hostInput.text()
    port = self.portInput.text()

    self.console.log(f"> Checking {host}:{port}")

    if check_tcp(host, port):
        self.statusLabel.setText("Open ✅")
        self.console.log("> Connection successful")
    else:
        self.statusLabel.setText("Закрыт ❌")
        self.console.log("> Connection failed")
