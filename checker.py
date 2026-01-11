import socket

def check_tcp(host, port):
    """
    # Checks a TCP connection to host:port
    # Returns True if the port is open, False if closed, None if the port is invalid

    """
    try:
        port = int(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except ValueError:
        return None
    except Exception:
        return False
