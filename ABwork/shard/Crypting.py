from cryptography.fernet import Fernet
 
# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 1

#Sec_key = "t+#v&+lgd@2%oek6hj&p7l^5r+99rgf@1yu@@o5=2p)szi*n)g"
key = b'6WkehmKJoctnEjTKDyQsnxDTb55ZmhJZlm9z8ZqCPvY='
#print(key)
fernet = Fernet(key)




    


