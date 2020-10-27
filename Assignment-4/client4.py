import socket

# creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# getting local machine name
host = socket.gethostname()                           

port = 8080

# connection to hostname on the port.
s.connect((host, port))       
#taking input from user                        
inputString = input("Enter the string for checking if it is a palindrome: ")
# sending input to convert lowercase to uppercase
s.send(inputString.encode('ascii'))
# Receiving the upper case string 1024 bytes at a time
outputString = (s.recv(1024))                                  

s.close()
print (outputString.decode('ascii'))