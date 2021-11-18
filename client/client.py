import logging
import socket

from shared.constants import SERVER_PORT, SERVER_ADDRESS, HEADER_SIZE, ENCODE_FORMAT

logging.basicConfig(level=logging.INFO, format='[%(asctime)s %(message)s', datefmt='%H:%M:%S')


class Client:

    def __init__(self, server_address, server_port):
        self.client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_connection.connect((server_address, server_port))
        message_length = self.client_connection.recv(HEADER_SIZE)
        message_length = int(message_length)
        welcome_message = self.client_connection.recv(message_length).decode(encoding=ENCODE_FORMAT)
        logging.info(f"RECEIVE MESSAGE]: {welcome_message}")
        
        name = input("Select one of the option : \n 1) open mode \n 2) secure mode \n 3) quit mode \n")
        while True:
            if name == "1" or 1: #determine mood
                self.client.send(bytes("1"),"utf-8") #send mood to server
                self.server_message = self.client.recv(1024).decode() #recive server mood response
                if self.server_message == "open mode ready": 
                    print("you are in open mood enter your message: ")

                    while True:
                        self.recive_user = input() # msg from user
                        if self.recive_user == "bye":
                            self.client.send(bytes(self.recive_user,"utf-8"))# close server connection
                            break #stop 
                        self.client.send(bytes(self.recive_user,"utf-8")) #send msg to server
                        self.r= self.client.recv(1024).decode() #recive server msg
                        print("message from server: "+ self.r) #print server msg



if __name__ == '__main__':
    client_connection = Client(server_address=SERVER_ADDRESS, server_port=SERVER_PORT)
