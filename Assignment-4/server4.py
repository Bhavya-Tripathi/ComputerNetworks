import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 8080                                          

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()  
   print("Connected to client:",clientsocket)    
   receivedData = ''
   # data received from client 1024 bytes at a time
   data = clientsocket.recv(1024).decode('ascii')
   #reversing data and checking to verify if it is a palindrome
   atad = data[::-1]
   if data == atad:
       msg = "The Input string " + data + " is a palindrome!"
   else : 
       msg = "The Input string " + data + " is not a palindrome!"
   # sending processed data to client
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()