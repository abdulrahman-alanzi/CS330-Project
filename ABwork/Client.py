import socket
from shard.Crypting import fernet
from cryptography.fernet import Fernet


def Client():					
    try:
        s = socket.socket()
        print ("Connection to server IP: "+ "localhost") # creat client sockt
    except socket.error as err:
        print ("socket creation failed with error %s" %(err)) # catch exception if any and display error msg


    server_port = 9999 # determine server port
    s.connect(("localhost",server_port)) #request conection
    mode = input("Please Enter the Communication Mode : \n 1) open mode \n 2) secure mode \n 3) quit mode \n") #client request

    #---------------------------------------------------------------------------------#
    #open mode
    if mode == '1': 
        s.send(bytes("1","utf-8")) #send mode to server
        server_message = s.recv(1024).decode() #recive server mood response
        if server_message == "Open Mode Ready": 

            print("Open Mode Ready, Enter your Message: ")
            recive_user = input("Enter your msg to server: ") # msg from user

            s.send(bytes(recive_user,"utf-8")) #send msg to server
            print('Send Message to server Successfully.')

            server_msg= s.recv(1024).decode() #recive server msg
            print("message from server: "+ server_msg) #print server msg
    #---------------------------------------------------------------------------------#
    #secure mode
    elif mode == '2': 
        s.send(bytes('2',"utf-8")) #send mode to server
        server_message = s.recv(1024).decode() #recive server mood response
        if server_message == "Secure Mode Ready": 

            print("Secure Mode Ready, Enter your Message: ")
            recive_user = input("Enter your msg to server: ") # msg from user
            encMessage = fernet.encrypt(recive_user.encode()) #encryptin msg
            
            

            s.send(encMessage) #send msg to server
            print('Send Message to server Successfully.')

            server_msg= s.recv(1024).decode() #recive server msg
            print("message from server: "+ server_msg) #print server msg
    #---------------------------------------------------------------------------------#
    #close connection
    elif mode == "3" or 3: 
        s.send(bytes("3","utf-8")) #send mode to server
        s.close()
        print('Connection With Client Closed')



Client()


