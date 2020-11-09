import socket,sys
print("Setting up server: ")

#Get hostname,IP
sock = socket.socket()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
port = 6969
sock.bind((hostname,port)) #binds IP of localhost to port
print(hostname, '({})'.format(ip))

name = input('Enter your name:')
sock.listen(1) #to locate using socket
print("Waiting for incoming connection. Please run the client program...")
conn,addr = sock.accept() #To accept the incoming connection.
#Code only allows for one client to be connected. Chat happend between server and client.

print('Recieved connection... Connected to {},({})'.format(addr[0],addr[1]))
#The .format thingy helps make code look neat, instead of having multiple string concatenations.

client = conn.recv(4096)
client = client.decode() # Receives the connection and gets the name.
print(client, "has connected.\nType 'exit' to exit the chat room")
conn.send(name.encode())

#Begin the infinite chat loop
while True:
    message = input('Me: ')
    if message == 'exit':
        message = "K bye then..."
        conn.send(message.encode())
        print("")
        break
    conn.send(message.encode())
    message = conn.recv(4096)
    message = message.decode()
    print(client,":",message)