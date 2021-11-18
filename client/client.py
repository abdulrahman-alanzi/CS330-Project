import socket

from shared.constants import SERVER_PORT, SERVER_ADDRESS


class Client:

    def __init__(self, server_address, server_port):
        self.server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_connection.connect((server_address, server_port))


if __name__ == '__main__':
    client_connection = Client(server_address=SERVER_ADDRESS, server_port=SERVER_PORT)
