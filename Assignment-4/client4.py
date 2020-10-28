import socket

#creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#getting local device info
host = socket.gethostname()

port = 5005

#get the palindrome string
data = input("Enter the string to test as a palindrome: ").encode('ascii')


s.sendto(data,(host,port)) #No "connect" is needed. Directly message bheja

data, addr = s.recvfrom(10240) #recv size is large...cause why not.
print(data)