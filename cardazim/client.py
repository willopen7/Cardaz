import argparse
import sys
import socket
import struct


###########################################################
####################### YOUR CODE #########################
###########################################################


def send_data(server_ip, server_port, data: bytes):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    data_size = len(data)
    byte_data_size = struct.pack("<I", data_size)
    client_socket.sendall(byte_data_size)
    client_socket.sendall(data)
    client_socket.close()


###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description="Send data to server.")
    parser.add_argument("server_ip", type=str, help="the server's ip")
    parser.add_argument("server_port", type=int, help="the server's port")
    parser.add_argument("data", type=str, help="the data")
    return parser.parse_args()


def main():
    """
    Implementation of CLI and sending data to server.
    """
    args = get_args()
    try:
        send_data(args.server_ip, args.server_port, args.data.encode("utf-8"))
        print("Done.")
    except Exception as error:
        print(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
