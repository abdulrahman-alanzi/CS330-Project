import socket
from shard.Crypting import fernet
from cryptography.fernet import Fernet
						
def Server():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creat server sockt
        print ("Server in Passive Mode - Listening")
    except socket.error as err:
        print ("socket creation failed with error %s" %(err)) # catch exception if any and display error msg


    server_port = 9999 # determine server port {port number range from 0 to 65535}
    s.bind(("localhost", server_port)) # bind ip and port for server
    s.listen(3) #number of client can be connect to server


    while True:
        conn, addr = s.accept() #accept connection
        print ("New Client Accepted",addr)
        msg = conn.recv(1024).decode() #recive mood from client
    #---------------------------------------------------------------------------------#
        #open mode
        if msg == '1' :
            print('Communicate With Client in Open Mode \n')
            conn.send(bytes("Open Mode Ready","utf-8")) #inform client by mode

            recive_client = conn.recv(1024).decode()#recive client msg
            print("Recived Message From Client: "+recive_client) #print client msg

            print('Return Message Back to Client: \n'+recive_client)
            conn.send(bytes(recive_client,"utf-8")) # send msg back to client
    
        #---------------------------------------------------------------------------------#
        #secure mode    
        elif msg == '2' :
            print('Communicate With Client in Secure Mode \n')
            conn.send(bytes("Secure Mode Ready","utf-8")) #inform client by mode

            recive_client = conn.recv(1024) #recive client msg
            rr = recive_client.decode()
            print("Recived Encripted Message From Client: "+ rr) #print client msg
            message = fernet.decrypt(recive_client).decode() #decripting client msg

            print(f'Return Message Back to Client After Decripte it: {message} \n')
            conn.send(bytes(message,"utf-8")) # send msg back to client
            
        #---------------------------------------------------------------------------------#
        #close connection   
        elif msg == '3' :
            print('Communication With Client Closed \n')
            s.close() #close connection
            break

Server()  


                    