import logging
import socket

from shared.constants import calculate_message_length, ENCODE_FORMAT


class HandleClient:
    def __init__(self, client_socket: socket.socket, address):
        self.socket_connection = client_socket
        self.address = address
        welcome_message = "WELCOME TO THE SERVER"
        message_length = calculate_message_length(welcome_message)
        self.socket_connection.send(message_length)
        self.socket_connection.send(welcome_message.encode(encoding=ENCODE_FORMAT))
        logging.info(f"SENDING]: welcome message to {self.address}")


def handle_client(client_socket, client_address):
    client = HandleClient(client_socket=client_socket, address=client_address)
