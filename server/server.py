import logging
import socket
import threading

from handle_client import handle_client
from shared.constants import SERVER_ADDRESS, SERVER_PORT

logging.basicConfig(level=logging.INFO, format='[%(asctime)s %(message)s', datefmt='%H:%M:%S')


class Server:
    def __init__(self, server_address: str, server_port: int):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((server_address, server_port))

    def run(self):
        self.server.listen()
        while True:
            client_socket, address = self.server.accept()
            logging.info(f"CLIENT CONNECTION]: Client connect with address {address}")
            thread = threading.Thread(target=handle_client, args=(client_socket, address))
            thread.start()


            
            name = self.server.recv(1024).decode() #recive mood from client
            if name == '1' :
                self.server.send(bytes("open mode ready","utf-8")) #inform client by mood
                
                while True:
                    self.r = self.server.recv(1024).decode()#recive client msg
                    if self.r == "bye":
                        self.server.close()#stop connection
                        break
                    print("message from client: "+self.r) #print client msg
                    self.recive_user = input() #msg from user
                    self.server.send(self.recive_user,"utf-8") # send user msg to client


if __name__ == '__main__':
    server = Server(SERVER_ADDRESS, SERVER_PORT)
    logging.info(f"SERVER START]: Server listen at {SERVER_ADDRESS}")
    server.run()
