import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 8000                                          

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      
   
   # data received from client 1024 bytes at a time
   data = clientsocket.recv(1024).decode('ascii')
   # getting the square and cube of the number
   square = (int(data))**2
   cube = (int(data))**3
   msg = "The square of the " + data + " is " + str(square) + " and its cube is " + str(cube)
   # sending processed data to client
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()