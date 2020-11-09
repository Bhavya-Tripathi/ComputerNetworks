import socket, sys
print("Setting up client...")

#get IP info and then bind to socket
sock = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)

#get info about server from client
print(host,'({})'.format(ip))
server = input("Enter Server's IP: ")
name = input("Enter your name: ")
port = 6969
print('Connecting to server...')
sock.connect((server,port))
print("Connected...")
sock.send(name.encode())
s_name = sock.recv(4096)
s_name = s_name.decode()

print('{} has joined...'.format(s_name))
print("Type 'exit' to quit.")

#begin loop
while True:
    message = sock.recv(4096)
    message = message.decode()
    print(s_name,":", message)
    message = input(str("Me: "))
    if message == 'exit':
        message = 'Leaving the Chat. Byeee'
        sock.send(message.encode())
        print("")
        break
    sock.send(message.encode())