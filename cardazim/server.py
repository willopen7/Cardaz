import socket
import argparse
import sys


def run_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen()
    print("Listening...")

    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    data_len = int.from_bytes(client_socket.recv(4), byteorder="little")
    msg = client_socket.recv(data_len).decode()
    print(f"Received data: {msg}")
    client_socket.close()
    server_socket.close()


def get_args():
    parser = argparse.ArgumentParser(description="Send data to server.")
    parser.add_argument("server_ip", type=str, help="the server's ip")
    parser.add_argument("server_port", type=int, help="the server's port")
    return parser.parse_args()


def main():
    """
    Implementation of CLI and receiving data from a client.
    """
    args = get_args()
    try:
        run_server(args.server_ip, args.server_port)
        print("Done.")
    except Exception as error:
        print(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
