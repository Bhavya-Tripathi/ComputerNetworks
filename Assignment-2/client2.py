import socket

# creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# getting local machine name
host = socket.gethostname()                           

port = 8000

# connection to hostname on the port.
s.connect((host, port))       
# taking input from user                        
inputNumber = str(input("Enter a number: "))
# sending input to server
s.send(inputNumber.encode('ascii'))
# Receiving the output from server 1024 bytes at a time
outputString = (s.recv(1024))                                  

s.close()
print (outputString.decode('ascii'))