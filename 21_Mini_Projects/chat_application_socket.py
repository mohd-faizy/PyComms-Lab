import argparse
import socket
import threading


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
        except OSError:
            break
        if not data:
            break
        print(data.decode("utf-8"))


def run_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(1)
        print(f"Server listening on {host}:{port}")
        conn, addr = server.accept()
        with conn:
            print(f"Client connected from {addr[0]}:{addr[1]}")
            threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
            while True:
                message = input()
                if message.lower() == "/quit":
                    break
                conn.sendall(f"server: {message}".encode("utf-8"))


def run_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        print(f"Connected to {host}:{port}")
        threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
        while True:
            message = input()
            if message.lower() == "/quit":
                break
            client.sendall(f"client: {message}".encode("utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Minimal TCP chat application")
    parser.add_argument("--mode", choices=["server", "client"], help="Run as server or client (optional)")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    mode = args.mode
    if not mode:
        # Auto-detect mode: try to connect as client first
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((args.host, args.port))
                mode = "client"
            except ConnectionRefusedError:
                mode = "server"
                
    if mode == "server":
        run_server(args.host, args.port)
    else:
        run_client(args.host, args.port)


if __name__ == "__main__":
    main()
