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
atad = data[::-1]   #reverses string
if data == atad:    #logic for checking palindrome or not.
    msg = "Yes the sent data was a palindrome"
else:
    msg = "No the sent data was not a palindrome" 
msg = msg.encode('ascii)') #encodes message for transmission
serversocket.sendto(msg,addr) #sends to the same port and address as the origin of the data
