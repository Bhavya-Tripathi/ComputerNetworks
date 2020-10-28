import socket

#create a socket object
serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#get local machine info
host = socket.gethostname()

port = 5005

#bind to port
serversocket.bind((host,port))


data,addr = serversocket.recvfrom(4096) #buffer size is 4096 bytes
print("Recieved Data is:", data,addr)

#test if data received is an integer 
try:                                
    int(data.decode('ascii'))

#raise error if not int
except ValueError:
    msg = "Sorry you did not send an integer"

#no errors then continue
else:
    data = int(data.decode('ascii')) #decodes the bytes type message and converts to int for processing
    if (data%2): 
        msg = "It is an odd integer"
    else:
        msg = "It is an even integer" 
msg = msg.encode('ascii)') #encodes message for transmission
serversocket.sendto(msg,addr) #sends to the same port and address as the origin of the data
